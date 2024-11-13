from playwright.sync_api import Playwright, sync_playwright, expect

#tickers = ["AAPL","AMZN","GM","HD","META","NET"]
def scrape_finance(playwright: Playwright, symbol:str, date:str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"https://finance.yahoo.com/quote/{symbol}/", timeout = 1000000)

    price_selector = page.query_selector("fin-streamer.livePrice")
    price = price_selector.inner_text()
    print(symbol, price)
    
    # ---------------------
    context.close()
    browser.close()
    
    return {"symbol": symbol, "price": price, "date": date}


with sync_playwright() as playwright:
    import pandas as pd
    folio = ["AAPL","AMZN","GM","HD","META","NET"]
    folio_data = []
    for symbol in folio:
        sym_data = scrape_finance(playwright, symbol, "2024-11-11")
        folio_data.append(sym_data)
    
    df=pd.DataFrame(folio_data)
    df.to_csv("folio_data.csv",index = False)