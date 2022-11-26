from script import IsDigit

user_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"}

try:
    import cloudscraper
except:
    DoInstall = input ("You did not install cloudscraper. Do you want to install it? (Y/N)\n");
    if (DoInstall == "Y" or DoInstall == "y"):
        import pip
        pip.main (["install", "cloudscraper"])
        import cloudscraper
    else:
        import sys
        sys.exit ()

if __name__ == "__main__":
    id_input = input ("Type in comic id.\n")
    if (IsDigit (id_input) == True):
        id = int (id_input)
    main_url = "https://nhentai.net/g/" + str (id) + "/1/"
    scraper = cloudscraper.create_scraper ()
    page = scraper.get (url = main_url, headers = user_headers)
    print (page.text)