import * as fs from 'fs'

export interface JSONData<T> {
    servers: T[]
}

/**
 * Função para ler, processar e enviar uma promise com o arquivo JSON 
 * 
 * @param path 
 * @return Promise<JSONData<string>>
 */
export function readJson(path: string): Promise<JSONData<string>>
{
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) {
                console.log('Erro ao ler arquivo: ', err)
                return
            }

            try {
                const objectJSON = JSON.parse(data)
                const servers = objectJSON.map((element: { Servidor: string }) => element.Servidor)
                resolve({ servers })
            } catch (error) {
                console.error('Erro ao analisar o conteúdo JSON: ', error)
                reject(error)
            }
        })
    })
}