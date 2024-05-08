import { chromium } from 'playwright'

/**
 * Classe responsavel pelo main
 */
class App
{
  /**
   * Metodo principal
   */
  public async main()
  {
    const browser = await chromium.launch({ headless: false })
    const page = await browser.newPage()
    await page.goto('https://www.iomat.mt.gov.br/legislacao/diario_oficial/1153/2024/')
    await page.waitForTimeout(3000)
    await page.locator('//*[@id="m_header_nav"]/a[1]').click()
    await page.waitForTimeout(1000)
    await page.locator('/html/body/div[2]/div[2]/div/div/div/div[4]/ul/li[1]/a[1]').click()

    await page.waitForTimeout(3000)
    await browser.close()
  }
}

const app = new App()
app.main()