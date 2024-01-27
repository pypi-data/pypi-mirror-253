"""
    The MIT License (MIT)

    Copyright (c) 2023 pkjmesra

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""
import logging
import sys
import warnings

import numpy as np

warnings.simplefilter("ignore", DeprecationWarning)
warnings.simplefilter("ignore", FutureWarning)
import pandas as pd
from PKDevTools.classes.ColorText import colorText
from PKDevTools.classes.Fetcher import StockDataEmptyException
from PKDevTools.classes.SuppressOutput import SuppressOutput
from PKDevTools.classes.PKDateUtilities import PKDateUtilities

import pkscreener.classes.Screener as Screener
import pkscreener.classes.Utility as Utility
from pkscreener import Imports
from pkscreener.classes.CandlePatterns import CandlePatterns


class StockConsumer:
    def __init__(self):
        self.isTradingTime = PKDateUtilities.isTradingTime()

    # @tracelog
    def screenStocks(
        self,
        executeOption,
        reversalOption,
        maLength,
        daysForLowestVolume,
        minRSI,
        maxRSI,
        respChartPattern,
        insideBarToLookback,
        totalSymbols,
        shouldCache,
        stock,
        newlyListedOnly,
        downloadOnly,
        volumeRatio,
        testbuild=False,
        printCounter=False,
        backtestDuration=0,
        backtestPeriodToLookback=30,
        logLevel=logging.NOTSET,
        portfolio=False,
        hostRef=None,
    ):
        assert (
            hostRef is not None
        ), "hostRef argument must not be None. It should b an instance of PKMultiProcessorClient"
        screeningDictionary, saveDictionary = self.initResultDictionaries()
        fullData = None
        processedData = None
        configManager = hostRef.configManager
        fetcher = hostRef.fetcher
        screener = hostRef.screener
        candlePatterns = hostRef.candlePatterns
        userArgsLog = printCounter
        try:
            if userArgsLog:
                self.setupLoggers(hostRef, screener, logLevel, stock)
            period = configManager.period
            if volumeRatio <= 0:
                volumeRatio = configManager.volumeRatio
            # Data download adjustment for Newly Listed only feature
            if newlyListedOnly:
                if int(configManager.period[:-1]) > 250:
                    period = "250d"
                else:
                    period = configManager.period
            # hostRef.default_logger.info(
            #     f"For stock:{stock}, stock exists in objectDictionary:{hostRef.objectDictionary.get(stock)}, cacheEnabled:{configManager.cacheEnabled}, isTradingTime:{self.isTradingTime}, downloadOnly:{downloadOnly}"
            # )
            hostData = hostRef.objectDictionary.get(stock)
            if (
                not shouldCache
                or downloadOnly
                or self.isTradingTime
                or hostData is None
            ) and (
                hostData is None and backtestDuration >= 0
            ):  # Fetch only if we are NOT backtesting
                start = None
                if (period == '1d' or configManager.duration[-1] == "m") and backtestDuration > 0:
                    start = PKDateUtilities.nthPastTradingDateStringFromFutureDate(backtestDuration)
                    end = start
                data = fetcher.fetchStockData(
                    stock,
                    period,
                    configManager.duration,
                    hostRef.proxyServer,
                    hostRef.processingResultsCounter,
                    hostRef.processingCounter,
                    totalSymbols,
                    start=start,
                    end=start
                )
                # hostRef.default_logger.info(f"Fetcher fetched stock data:\n{data}")
                if (
                    (shouldCache and not self.isTradingTime and (hostData is None))
                    or downloadOnly
                ) or (
                    shouldCache and hostData is None
                ):  # and backtestDuration == 0 # save only if we're NOT backtesting
                    if start is None and data is not None:
                        # Don't need to save if it's not for today. Save only for today
                        hostRef.objectDictionary[stock] = data.to_dict("split")
                    # hostRef.default_logger.info(
                    #     f"Stock data saved:\n{hostRef.objectDictionary[stock]}"
                    # )
                    if downloadOnly:
                        with hostRef.processingResultsCounter.get_lock():
                            hostRef.processingResultsCounter.value += 1
                        raise Screener.DownloadDataOnly
                    else:
                        hostData = hostRef.objectDictionary.get(stock)
            else:
                if printCounter:
                    try:
                        print(
                            colorText.BOLD
                            + colorText.GREEN
                            + (
                                "[%d%%] Screened %d, Found %d. Fetching data & Analyzing %s..."
                                % (
                                    int(
                                        (hostRef.processingCounter.value / totalSymbols)
                                        * 100
                                    ),
                                    hostRef.processingCounter.value,
                                    hostRef.processingResultsCounter.value,
                                    stock,
                                )
                            )
                            + colorText.END,
                            end="",
                        )
                        print(
                            colorText.BOLD
                            + colorText.GREEN
                            + "=> Done!"
                            + colorText.END,
                            end="\r",
                            flush=True,
                        )
                    except ZeroDivisionError as e:
                        hostRef.default_logger.debug(e, exc_info=True)
                        pass
                    sys.stdout.write("\r\033[K")
                data = hostData
                data = pd.DataFrame(
                    data["data"], columns=data["columns"], index=data["index"]
                )
            if len(data) == 0 or len(data) < backtestDuration:
                return None
            # hostRef.default_logger.info(f"Will pre-process data:\n{data.tail(10)}")
            if backtestDuration == 0:
                fullData, processedData = screener.preprocessData(
                    data, daysToLookback=configManager.daysToLookback
                )
            else:
                if data is None or fullData is None or processedData is None:
                    # data will have the oldest date at the top and the most recent
                    # date will be at the bottom
                    # We want to have the nth day treated as today when pre-processing where n = backtestDuration row from the bottom
                    inputData = data.head(len(data) - backtestDuration)
                    # imputData will have the last row as the date for which the entire calculation
                    # and prediction is being done
                    data = data.tail(
                        backtestDuration + 1
                    )  # .head(backtestPeriodToLookback+1)
                    # Let's get today's data
                    if portfolio:
                        screener.validateLTPForPortfolioCalc(
                            data, screeningDictionary, saveDictionary
                        )
                    # data has the last row from inputData at the top.
                    fullData, processedData = screener.preprocessData(
                        inputData, daysToLookback=configManager.daysToLookback
                    )
            # hostRef.default_logger.info(
            #     f"Finished pre-processing. processedData:\n{data}\nfullData:{fullData}\n"
            # )
            if newlyListedOnly:
                if not screener.validateNewlyListed(fullData, period):
                    raise Screener.NotNewlyListed

            with hostRef.processingCounter.get_lock():
                hostRef.processingCounter.value += 1
                # hostRef.default_logger.info(
                #     f"Processing {stock} in {hostRef.processingCounter.value}th counter"
                # )
            if not processedData.empty:
                screeningDictionary["Stock"] = (
                    colorText.WHITE
                    + (
                        f"\x1B]8;;https://in.tradingview.com/chart?symbol=NSE%3A{stock}\x1B\\{stock}\x1B]8;;\x1B\\"
                    )
                    + colorText.END
                )
                saveDictionary["Stock"] = stock
                if not self.shouldProceedWithScanning(executeOption):
                    return None
                
                isLtpValid, verifyStageTwo = screener.validateLTP(
                    fullData,
                    screeningDictionary,
                    saveDictionary,
                    minLTP=configManager.minLTP,
                    maxLTP=configManager.maxLTP,
                )
                if not isLtpValid:
                    raise Screener.LTPNotInConfiguredRange
                if configManager.stageTwo and not verifyStageTwo and executeOption > 0:
                    raise Screener.NotAStageTwoStock
                minVolume = configManager.minVolume / (
                    100 if configManager.isIntradayConfig() else 1
                )
                hasMinVolumeRatio, hasMinVolQty = screener.validateVolume(
                    processedData,
                    screeningDictionary,
                    saveDictionary,
                    volumeRatio=volumeRatio,
                    minVolume=minVolume,
                )
                if (not hasMinVolQty and executeOption > 0) or (executeOption == 9 and not hasMinVolumeRatio):
                    raise Screener.NotEnoughVolumeAsPerConfig
                
                isConfluence = False
                isInsideBar = 0
                isIpoBase = False
                isMaSupport = False
                isShortTermBullish = False
                isLorentzian = False
                isVCP = False
                isVSA = False
                isNR = False
                isBuyingTrendline = False

                if executeOption == 11:
                    isShortTermBullish = screener.validateShortTermBullish(
                        fullData, screeningDictionary, saveDictionary
                    )
                    if not isShortTermBullish:
                        return None
                if executeOption == 12:
                    is15MinutePriceVolumeBreakout = (
                        screener.validate15MinutePriceVolumeBreakout(fullData)
                    )
                    if not is15MinutePriceVolumeBreakout:
                        return None
                if executeOption == 13:
                    isBullishIntradayRSIMACD = screener.findBullishIntradayRSIMACD(
                        fullData
                    )
                    if not isBullishIntradayRSIMACD:
                        return None
                if executeOption == 14:
                    isNR4Day = screener.findNR4Day(fullData)
                    if not isNR4Day:
                        return None
                if executeOption == 15:
                    is52WeekLowBreakout = screener.find52WeekLowBreakout(fullData)
                    if not is52WeekLowBreakout:
                        return None
                if executeOption == 16:
                    is10DaysLowBreakout = screener.find10DaysLowBreakout(fullData)
                    if not is10DaysLowBreakout:
                        return None
                if executeOption == 17:
                    is52WeekHighBreakout = screener.find52WeekHighBreakout(fullData)
                    if not is52WeekHighBreakout:
                        return None
                if executeOption == 18:
                    isAroonCrossover = screener.findAroonBullishCrossover(fullData)
                    if not isAroonCrossover:
                        return None
                if executeOption == 19:
                    macdHistBelow0 = screener.validateMACDHistogramBelow0(fullData)
                    if not macdHistBelow0:
                        return None
                if executeOption == 20:
                    bullishForTomorrow = screener.validateBullishForTomorrow(fullData)
                    if not bullishForTomorrow:
                        return None
                if executeOption == 23:
                    isBreakingOutNow = screener.findBreakingoutNow(processedData)
                    if not isBreakingOutNow:
                        return None
                if executeOption == 24:
                    higherHighsLowsClose = (
                        screener.validateHigherHighsHigherLowsHigherClose(fullData)
                    )
                    if not higherHighsLowsClose:
                        return None
                if executeOption == 25:
                    hasLowerLows = screener.validateLowerHighsLowerLows(processedData)
                    if not hasLowerLows:
                        return None
                
                if executeOption == 4:
                    isLowestVolume = screener.validateLowestVolume(
                        processedData, daysForLowestVolume
                    )
                    if not isLowestVolume:
                        return None
                else:
                    isLowestVolume = False
                if executeOption == 4 and (not isLowestVolume):
                    return None
                
                isValidRsi = screener.validateRSI(
                    processedData, screeningDictionary, saveDictionary, minRSI, maxRSI
                )
                if executeOption == 5 and (not isValidRsi):
                    return None

                if newlyListedOnly:
                    isIpoBase = screener.validateIpoBase(
                        stock, fullData, screeningDictionary, saveDictionary
                    )

                if executeOption == 7:
                    if respChartPattern == 3:
                        isConfluence = screener.validateConfluence(
                            stock,
                            processedData,
                            screeningDictionary,
                            saveDictionary,
                            percentage=insideBarToLookback,
                        )
                        if not isConfluence:
                            return None

                with SuppressOutput(suppress_stderr=True, suppress_stdout=True):
                    if (executeOption == 6
                        and reversalOption == 6
                    ):
                        isNR = screener.validateNarrowRange(
                            processedData,
                            screeningDictionary,
                            saveDictionary,
                            nr=maLength if maLength is not None else 4,
                        )
                        if not isNR:
                            return None

                if executeOption == 10:
                    isPriceRisingByAtLeast2Percent = (
                        screener.validatePriceRisingByAtLeast2Percent(
                            processedData, screeningDictionary, saveDictionary
                        )
                    )
                    if not isPriceRisingByAtLeast2Percent:
                        return None

                isVSA = False
                if (executeOption == 6 and reversalOption == 5):
                    isVSA = screener.validateVolumeSpreadAnalysis(
                        processedData, screeningDictionary, saveDictionary
                    )
                    if not isVSA:
                        return None
                    
                if executeOption == 6 and reversalOption == 4 and maLength is not None:
                    isMaSupport = screener.findReversalMA(
                        fullData, screeningDictionary, saveDictionary, maLength
                    )
                    if not isMaSupport:
                        return None

                isVCP = False
                if executeOption == 7 and respChartPattern == 4:
                    with SuppressOutput(suppress_stderr=True, suppress_stdout=True):
                        isVCP = screener.validateVCP(
                            fullData, screeningDictionary, saveDictionary
                        )
                        if not isVCP:
                            return None

                isBuyingTrendline = False
                if executeOption == 7 and respChartPattern == 5:
                    with SuppressOutput(suppress_stderr=True, suppress_stdout=True):
                        if Imports["scipy"]:
                            isBuyingTrendline = screener.findTrendlines(
                                fullData, screeningDictionary, saveDictionary
                            )
                            if not isBuyingTrendline:
                                return None
                if sys.version_info >= (3, 11):
                    with SuppressOutput(suppress_stderr=True, suppress_stdout=True):
                        isLorentzian = screener.validateLorentzian(
                            fullData,
                            screeningDictionary,
                            saveDictionary,
                            lookFor=maLength, # 1 =Buy, 2 =Sell, 3 = Any
                        )
                        if executeOption == 6 and reversalOption == 7 and not isLorentzian:
                            return None
                else:
                    isLorentzian = False
                
                isBreaking = screener.findBreakoutValue(
                    processedData,
                    screeningDictionary,
                    saveDictionary,
                    daysToLookback=configManager.daysToLookback,
                    alreadyBrokenout=(executeOption == 2),
                )
                if executeOption == 1:
                    isPotentialBreaking = screener.findPotentialBreakout(
                        fullData,
                        screeningDictionary,
                        saveDictionary,
                        daysToLookback=configManager.daysToLookback,
                    )
                    if not (isBreaking or isPotentialBreaking) or not hasMinVolumeRatio:
                        return None
                elif executeOption == 2:
                    if not (isBreaking) or not hasMinVolumeRatio:
                        return None
                    
                consolidationValue = screener.validateConsolidation(
                    processedData,
                    screeningDictionary,
                    saveDictionary,
                    percentage=configManager.consolidationPercentage,
                )
                if ((executeOption == 3)
                        and (
                            consolidationValue == 0 or
                            consolidationValue > configManager.consolidationPercentage
                        )
                    ):
                    return None
                
                # Must-run, but only at the end
                isCandlePattern = False
                try:
                    # Only 'doji' and 'inside' is internally implemented by pandas_ta.
                    # Otherwise, for the rest of the candle patterns, they also need
                    # TA-Lib. So if TA-Lib is not available, it will throw exception
                    # We can live with no-patterns if user has not installed ta-lib
                    # yet. If ta-lib is available, PKTalib will load it automatically.
                    isCandlePattern = candlePatterns.findPattern(
                        processedData, screeningDictionary, saveDictionary
                    )
                except Exception as e:  # pragma: no cover
                    hostRef.default_logger.debug(e, exc_info=True)
                    screeningDictionary["Pattern"] = ""
                    saveDictionary["Pattern"] = ""
                if executeOption == 6:
                    if reversalOption == 1 and not (str(saveDictionary["Pattern"]).split(",")[0]
                                                                    in CandlePatterns.reversalPatternsBullish
                                                                    or isMaReversal > 0):
                        return None
                    elif reversalOption == 2 and not (str(saveDictionary["Pattern"]).split(",")[0]
                                                                    in CandlePatterns.reversalPatternsBearish
                                                                    or isMaReversal < 0):
                        return None
                
                try:
                    with SuppressOutput(suppress_stderr=True, suppress_stdout=True):
                        currentTrend = screener.findTrend(
                            processedData,
                            screeningDictionary,
                            saveDictionary,
                            daysToLookback=configManager.daysToLookback,
                            stockName=stock,
                        )
                except np.RankWarning as e:
                    hostRef.default_logger.debug(e, exc_info=True)
                    screeningDictionary["Trend"] = "Unknown"
                    saveDictionary["Trend"] = "Unknown"
                # CCI also uses "Trend" value from findTrend above.
                # So it must only be called after findTrend
                isValidCci = screener.validateCCI(
                    processedData, screeningDictionary, saveDictionary, minRSI, maxRSI
                )
                if executeOption == 8 and not isValidCci:
                    return None

                if not (isConfluence or isShortTermBullish or isMaSupport):
                    isMaReversal = screener.validateMovingAverages(
                        processedData, screeningDictionary, saveDictionary, maRange=1.25
                    )
                # validateInsideBar needs "Trend" to be already defined
                # ValidateInsideBar also needs "MA-Signal" to be setup
                if executeOption == 7 and respChartPattern < 3:
                    isInsideBar = screener.validateInsideBar(
                                processedData,
                                screeningDictionary,
                                saveDictionary,
                                chartPattern=respChartPattern,
                                daysToLookback=insideBarToLookback,
                            )
                    if isInsideBar ==0:
                        return None

                if not (isLorentzian or (isInsideBar !=0) or isBuyingTrendline or isIpoBase or isNR or isVCP or isVSA):
                    isMomentum = screener.validateMomentum(
                        processedData, screeningDictionary, saveDictionary
                    )
                    if executeOption == 6 and reversalOption ==3 and not isMomentum:
                        return None

                screener.find52WeekHighLow(
                    fullData, saveDictionary, screeningDictionary
                )

                with hostRef.processingResultsCounter.get_lock():
                    # hostRef.default_logger.info(
                    #     f"Processing results for {stock} in {hostRef.processingResultsCounter.value}th results counter"
                    # )
                    if (
                        (executeOption == 0)
                        or ((
                            (
                                (executeOption == 1 and (isBreaking or isPotentialBreaking))
                                or (executeOption == 2 and isBreaking)
                            )
                            and hasMinVolumeRatio
                        ))
                        or ((
                            (executeOption == 3)
                            and (
                                consolidationValue <= configManager.consolidationPercentage
                                and consolidationValue != 0
                            )
                        ))
                        or (executeOption == 4 and isLowestVolume)
                        or (executeOption == 5 and isValidRsi)
                        or ((executeOption == 6) and ((reversalOption == 1 and (
                                                                    str(saveDictionary["Pattern"]).split(",")[0]
                                                                    in CandlePatterns.reversalPatternsBullish
                                                                    or isMaReversal > 0
                                                                ))
                                                                or (reversalOption == 2 and (
                                                                    str(saveDictionary["Pattern"]).split(",")[0]
                                                                    in CandlePatterns.reversalPatternsBearish
                                                                    or isMaReversal < 0
                                                                ))
                                                                or (reversalOption == 3 and isMomentum)
                                                                or (reversalOption == 4 and isMaSupport)
                                                                or ((
                                                                    reversalOption == 5
                                                                    and isVSA
                                                                    and saveDictionary["Pattern"]
                                                                    in CandlePatterns.reversalPatternsBullish
                                                                ))
                                                                or (reversalOption == 6 and isNR)
                                                                or (reversalOption == 7 and isLorentzian)
                                                                ))
                        or ((executeOption == 7) and ((respChartPattern < 3 and isInsideBar >0) 
                                                                  or (isConfluence)
                                                                  or (isIpoBase and newlyListedOnly and not respChartPattern < 3)
                                                                  or (isVCP)
                                                                  or (isBuyingTrendline)))
                        or (executeOption == 8 and isValidCci)
                        or (executeOption == 9 and hasMinVolumeRatio)
                        or (executeOption == 10 and isPriceRisingByAtLeast2Percent)
                        or (executeOption == 11 and isShortTermBullish)
                        or (executeOption == 12 and is15MinutePriceVolumeBreakout)
                        or (executeOption == 13 and isBullishIntradayRSIMACD)
                        or (executeOption == 14 and isNR4Day)
                        or (executeOption == 15 and is52WeekLowBreakout)
                        or (executeOption == 16 and is10DaysLowBreakout)
                        or (executeOption == 17 and is52WeekHighBreakout)
                        or (executeOption == 18 and isAroonCrossover)
                        or (executeOption == 19 and macdHistBelow0)
                        or (executeOption == 20 and bullishForTomorrow)
                        or (executeOption == 23 and isBreakingOutNow)
                        or (executeOption == 24 and higherHighsLowsClose)
                        or (executeOption == 25 and hasLowerLows)
                    ):
                        hostRef.processingResultsCounter.value += 1
                        return (
                            screeningDictionary,
                            saveDictionary,
                            data,
                            stock,
                            backtestDuration,
                        )

        except KeyboardInterrupt: # pragma: no cover
            # Capturing Ctr+C Here isn't a great idea
            pass
        except StockDataEmptyException as e: # pragma: no cover
            hostRef.default_logger.debug(e, exc_info=True)
            pass
        except Screener.NotNewlyListed as e: # pragma: no cover
            hostRef.default_logger.debug(e, exc_info=True)
            pass
        except Screener.NotAStageTwoStock as e: # pragma: no cover
            # hostRef.default_logger.debug(e, exc_info=True)
            pass
        except Screener.NotEnoughVolumeAsPerConfig as e:
            pass
        except Screener.DownloadDataOnly as e: # pragma: no cover
            # hostRef.default_logger.debug(e, exc_info=True)
            pass
        except Screener.LTPNotInConfiguredRange as e: # pragma: no cover
            # hostRef.default_logger.debug(e, exc_info=True)
            pass
        except KeyError as e: # pragma: no cover
            hostRef.default_logger.debug(e, exc_info=True)
            pass
        except OSError as e: # pragma: no cover
            pass
        except Exception as e:  # pragma: no cover
            hostRef.default_logger.debug(e, exc_info=True)
            if testbuild or printCounter:
                print(e)
                print(
                    colorText.FAIL
                    + (
                        "\n[+] Exception Occured while Screening %s! Skipping this stock.."
                        % stock
                    )
                    + colorText.END
                )
        return None

    def shouldProceedWithScanning(self, executeOption=None):
        proceed = True
        
        return proceed
    
    def setupLoggers(self, hostRef, screener, logLevel, stock):
        # Set the loglevels for both the caller and screener
        # Also add handlers that are specific to this sub-process which
        # will co ntinue with the screening. Each sub-process would have
        # its own logger but going into the same file/console > to that
        # of the parent logger.
        if hostRef.default_logger.level > 0:
            return
        hostRef.default_logger.level = logLevel
        screener.default_logger.level = logLevel
        hostRef.default_logger.addHandlers(log_file_path=None, levelname=logLevel)
        screener.default_logger.addHandlers(log_file_path=None, levelname=logLevel)
        hostRef.default_logger.info(f"Beginning the stock screening for stock:{stock}")

    def initResultDictionaries(self):
        periods = [1, 2, 3, 4, 5, 10, 15, 22, 30]
        columns = [
            "Stock",
            "Consol.",
            "Breakout",
            "MA-Signal",
            "Volume",
            "LTP",
            "52Wk H",
            "52Wk L",
            "%Chng",
            "RSI",
            "Trend",
            "Pattern",
            "CCI",
        ]
        screeningDictionary = {
            "Stock": "",
            "Consol.": "",
            "Breakout": "",
            "MA-Signal": "",
            "Volume": "",
            "LTP": 0,
            "52Wk H": 0,
            "52Wk L": 0,
            "%Chng": 0,
            "RSI": 0,
            "Trend": "",
            "Pattern": "",
            "CCI": 0,
        }
        saveDictionary = {
            "Stock": "",
            "Consol.": "",
            "Breakout": "",
            "MA-Signal": "",
            "Volume": "",
            "LTP": 0,
            "52Wk H": 0,
            "52Wk L": 0,
            "%Chng": 0,
            "RSI": 0,
            "Trend": "",
            "Pattern": "",
            "CCI": 0,
        }
        for prd in periods:
            columns.append(f"LTP{prd}")
            columns.append(f"Growth{prd}")
            screeningDictionary[f"LTP{prd}"] = np.nan
            saveDictionary[f"LTP{prd}"] = np.nan
            screeningDictionary[f"Growth{prd}"] = np.nan
            saveDictionary[f"Growth{prd}"] = np.nan

        screenResults = pd.DataFrame(columns=columns)

        return screeningDictionary, saveDictionary
