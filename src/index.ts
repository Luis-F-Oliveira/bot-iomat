import { chromium } from 'playwright'
import { readJson } from './lib/typescript/readjson';

interface ISavedData {
  order: string
  url: string
  names: string[]
}

/**
 * Classe responsavel pelo main
 */
class App
{
  private savedData: ISavedData[]

  /**
   * Construtor da classe
   */
  constructor()
  {
    this.savedData = []
  }

  /**
   * Metodo principal
   */
  public async main()
  {
    function removeAccents(text: string) {
      return text
       .normalize('NFD')
       .replace(/[\u0300-\u036f]/g, '')
    }

    function processText(text: string) {
      return removeAccents(text)
      .toLowerCase()
    }

    const data = await readJson('./json/servers.json')
    const servers = data.servers

    const browser = await chromium.launch({ headless: false })
    const page = await browser.newPage()
    await page.goto('https://www.iomat.mt.gov.br/legislacao/diario_oficial/1153/2024/')

    await page.locator('xpath=/html/body/div[2]/div[2]/div/div/div/div[4]/ul/li[1]/a[1]').click()

    const matter: string[] = []
    const text = await page.locator('xpath=/html/body/div[2]/div[3]/div/div/div/div').innerText()
    const textProcessed = processText(text)
    matter.push(textProcessed)

    const foundNames = servers.filter((server: string) => 
      matter.some((name: string) => name.includes(server))
    )

    const order = await page.locator('xpath=/html/body/div[2]/div[3]/div/div/div/div/p[1]/span').innerText()
    const url = page.url()

    this.savedData.push({ 
      order: order,
      url: url,
      names: foundNames
    })

    console.log(this.savedData)

    await page.waitForTimeout(3000)
    await browser.close()
  }
}

const app = new App()
app.main()



  