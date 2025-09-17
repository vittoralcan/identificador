import fitz

def gerar_relatorio_ocr(caminho_pdf):
    relatorio = []
    
    try:
        documento = fitz.open(caminho_pdf)
        total_paginas = len(documento)
        
        print(f"Iniciando análise de OCR para {total_paginas} páginas...\n")
        
        for num_pagina, pagina in enumerate(documento):
            texto = pagina.get_text()
            status_ocr = ""
            
            # Verifica se o texto da página está vazio ou contém apenas espaços.
            if not texto.strip():
                status_ocr = "não possui OCR"
            else:
                status_ocr = "possui OCR"
                
            # Adiciona a linha ao relatório no formato desejado.
            relatorio.append(f"{num_pagina + 1}: {status_ocr}")
                
        documento.close()
        return relatorio

    except FileNotFoundError:
        return [f"Erro: O arquivo '{caminho_pdf}' não foi encontrado."]


if __name__ == "__main__":
    caminho_do_arquivo_pdf = "seu_documento.pdf"
    
    relatorio_ocr = gerar_relatorio_ocr(caminho_do_arquivo_pdf)

    for linha in relatorio_ocr:
        print(linha)
    
    # Para saber apenas o total de páginas sem OCR.
    paginas_sem_ocr = [linha for linha in relatorio_ocr if "não possui OCR" in linha]
    print("\n" + "="*50)
    print(f"Total de páginas sem OCR: {len(paginas_sem_ocr)}")
    print("Prontinho minha princesa❤️")