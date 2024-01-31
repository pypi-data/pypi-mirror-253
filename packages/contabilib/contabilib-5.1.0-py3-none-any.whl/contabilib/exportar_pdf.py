import fpdf

# Vamos importar o FPDF dentro de cada função onde é necessário
def create_pdf_rescisao(file_name, data):
    from fpdf import FPDF

    '''Este método cria um PDF com os dados da rescisão.'''
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Termo de Rescisão do Contrato de Trabalho', 0, 1, 'C')
    pdf.ln(10)

    pdf.set_fill_color(200, 200, 200)  # Cinza claro
    th = 10
    pdf.set_font('Times', '', 14)

    for i, row in enumerate(data):
        if i % 2 == 0:
            pdf.set_fill_color(200, 200, 200)  # Cinza claro para linhas pares
        else:
            pdf.set_fill_color(255, 255, 255)  # Branco para linhas ímpares
        pdf.cell(90, th, str(row[0]), border=1, ln=0, fill=True)
        pdf.cell(0, th, str(row[1]), border=1, ln=1, fill=True)

    pdf.ln(10)
    pdf.cell(0, th, 'Assinatura do Funcionário: ________________________', 0, 1)
    pdf.cell(0, th, 'Assinatura do Empregador: ________________________', 0, 1)
    pdf.output(file_name)


def gerar_pdf_rescisao(nome, cpf, razaosocial, cnpj, tempodeservico, salario, causadoafastamento, multafgts, avisoprevio, decimoterceiro,
                       ferias_proporcionais, diadarescisao, valor_rescisao):
    '''Este método gera um PDF com os dados da rescisão.'''
    multafgts = str(multafgts)
    valor_rescisao = str(valor_rescisao)
    avisoprevio = str(avisoprevio)
    decimoterceiro = str(decimoterceiro)
    ferias_proporcionais = str(ferias_proporcionais)
    salario = str(salario)

    data = [
        ['Nome do Funcionário', nome],
        ['CPF', cpf],
        ['Razão Social da Empresa', razaosocial],
        ['CNPJ', cnpj],
        ['Tempo de Serviço', tempodeservico],
        ['Dia da Rescisão', diadarescisao],
        ['Causa do Afastamento', causadoafastamento],
        ['Salário', 'R$ ' + salario],
        ['Multa FGTS', 'R$ ' + multafgts],
        ['Aviso Prévio', 'R$ ' + avisoprevio],
        ['Décimo Terceiro', 'R$ ' + decimoterceiro],
        ['Férias Proporcionais', 'R$ ' + ferias_proporcionais],
        ['Valor da Rescisão', 'R$ ' + valor_rescisao],
    ]

    create_pdf_rescisao("termo_de_rescisao.pdf", data)


def create_pdf_balanco(file_name, data):
    from fpdf import FPDF

    '''Cria um PDF com os dados do balanço patrimonial.'''
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Balanço Patrimonial', 0, 1, 'C')
    pdf.ln(10)

    pdf.set_fill_color(200, 200, 200)  # Cinza claro
    th = 10
    pdf.set_font('Times', '', 14)

    for i, row in enumerate(data):
        if i % 2 == 0:
            pdf.set_fill_color(200, 200, 200)  # Cinza claro para linhas pares
        else:
            pdf.set_fill_color(255, 255, 255)  # Branco para linhas ímpares
        pdf.cell(90, th, str(row[0]), border=1, ln=0, fill=True)
        pdf.cell(0, th, str(row[1]), border=1, ln=1, fill=True)

    pdf.output(file_name)


def gerar_pdf_balanco(ativos, passivos, periodo):
    from fpdf import FPDF

    '''Este método gera um PDF com os dados do balanço patrimonial.'''
    data = []
    patrimonio_liquido_total = 0
    for mes in periodo:
        ativo_circulante = ativos[mes]['ativo_circulante']
        ativo_nao_circulante = ativos[mes]['ativo_nao_circulante']
        passivo_circulante = passivos[mes]['passivo_circulante']
        passivo_nao_circulante = passivos[mes]['passivo_nao_circulante']
        patrimonio_liquido = ativo_circulante + ativo_nao_circulante - \
            passivo_circulante - passivo_nao_circulante
        patrimonio_liquido_total += patrimonio_liquido

        data.append([f"Ativo Circulante ({mes})", f"R$ {ativo_circulante}"])
        data.append(
            [f"Ativo Não Circulante ({mes})", f"R$ {ativo_nao_circulante}"])
        data.append(
            [f"Passivo Circulante ({mes})", f"R$ {passivo_circulante}"])
        data.append(
            [f"Passivo Não Circulante ({mes})", f"R$ {passivo_nao_circulante}"])
        data.append(
            [f"Patrimônio Líquido ({mes})", f"R$ {patrimonio_liquido}"])
        data.append(["", ""])  # linha em branco entre os meses

    data.append(["Patrimônio Líquido Total", f"R$ {patrimonio_liquido_total}"])

    create_pdf_balanco("balanco_patrimonial.pdf", data)
