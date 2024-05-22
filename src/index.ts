import { chromium } from 'playwright'
import { readJson } from './lib/typescript/readjson'
import * as fs from 'fs'

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

    const date = new Date()
    const formattedDate = date.toLocaleDateString('pt-BR')

    const data = await readJson('./json/servers.json')
    const servers = data.servers

    const browser = await chromium.launch({ headless: false })
    const page = await browser.newPage()
    await page.goto('https://www.iomat.mt.gov.br/legislacao/diario_oficial/1153/2024/')

    await page.locator('xpath=/html/body/div[2]/div[2]/div/div/div/div[4]/ul/li[1]/a[1]').click()

    while (true) {
      const a = page.locator('xpath=/html/body/div[2]/div[1]/div/div[1]/a')
      const aText = await a.innerText()
      if (aText.includes(formattedDate)) {
        a.click()
        await page.waitForTimeout(3000)
        const matter: string[] = []
        const text = await page.locator('xpath=/html/body/div[2]/div[3]/div/div/div/div').innerText()
        const textProcessed = processText(text)
        matter.push(textProcessed)

        const foundNames = servers.filter((server: string) => 
          matter.some((name: string) => name.includes(server))
        )

        const order = await page.locator('xpath=/html/body/div[2]/div[1]/div/div[2]/h4').innerText()
        const url = page.url()

        this.savedData.push({ 
          order: order,
          url: url,
          names: foundNames
        })
      } else {
        break
      }
    }

    this.savedData.forEach(obj => {
      obj.names = obj.names.filter(name => name !== 'nan')
    })

    const jsonData = JSON.stringify(this.savedData, null, 2)

    fs.writeFile('./json/savedData.json', jsonData, err => {
      if (err) {
        console.log('Erro ao salvar arquivo: ', err)
        return
      }
      console.log('Arquivo salvo com sucesso!')
    })

    await page.waitForTimeout(3000)
    await browser.close()
  }
}

const app = new App()
app.main()



  