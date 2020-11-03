# outputs
These are sample outputs from **oneSearch.py**. **googleTest.py** will have the same outputs, but **googleTest.py** may not recognize all the tickers (in this case ^GSPC).

<br />*NOTE: These do not have the correct spacing on readme, but if you look at the actual file it will have the correct spacing.*

**oct072020.txt** using "-s" flag:

> WARNING 1001 - Stock (XFGA) value not found
> <br />Using 0 for price...
> <br />
> <br />=================================================
> <br />Stock |      Total Value      |     Change
> <br />=================================================
> <br />AAPL  | $            2,301.60 |           -(2.80)
> <br />TSLA  | $           10,632.50 |         +(111.00)
> <br />XFGA  | $                0.00 |           +(0.00)
> <br />^GSPC | $           17,096.95 |          +(15.00)
> <br />SPX   | $           17,096.95 |          +(15.05)
> <br />=================================================
> <br />Total | $           47,128.00 |         +(138.25)
> <br />=================================================

<br />**oct092020.txt** using "-c" flag:

> WARNING 1001 - Stock (XFGA) value not found
> <br />Using 0 for price...
> <br />
> <br />=================================================
> <br />Stock |      Total Value      |     Change
> <br />=================================================
> <br />AAPL  | $            2,339.40 |             37.80
> <br />TSLA  | $           10,848.75 |            216.25
> <br />XFGA  | $                0.00 |              0.00
> <br />^GSPC | $           17,385.55 |            288.60
> <br />SPX   | $           17,385.55 |            288.60
> <br />=================================================
> <br />Total | $           47,959.25 |            831.25
> <br />=================================================

<br />What using no flag for print type looks like:

> WARNING 1001 - Stock (XFGA) value not found
> <br />Using 0 for price...
> <br />
> <br />=============================
> <br />Stock |      Total Value
> <br />=============================
> <br />AAPL  | $            2,339.40
> <br />TSLA  | $           10,848.75
> <br />XFGA  | $                0.00
> <br />^GSPC | $           17,385.55
> <br />SPX   | $           17,385.55 
> <br />=============================
> <br />Total | $           47,959.25 
> <br />=============================
