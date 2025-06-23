import pandas as pd
from app.models import Institution, InvestmentTitle, WeeklyQuote

def parse_excel(file_path, session):
    excel_data = pd.ExcelFile(file_path)

    for sheet_name in excel_data.sheet_names:
        df = excel_data.parse(sheet_name)

        for _, row in df.iterrows():
            inst_name = row.get("Instituicao") or "Unknown"
            title_code = row.get("codTitulo") or row.get("Título") or "Sem código"

            # Buscar ou criar instituição
            institution = session.query(Institution).filter(Institution.name == inst_name).first()
            if not institution:
                institution = Institution(name=inst_name)
                session.add(institution)
                session.flush()

            # Criar título
            title = InvestmentTitle(
                code=title_code,
                description=row.get("Título", ""),
                type_title=row.get("TipoTitulo", "Desconhecido"),
                institution=institution
            )
            session.add(title)
            session.flush()

            # Criar cotação
            quote = WeeklyQuote(
                date=sheet_name,
                quantity=row.get("Qtd", 1),
                value=float(str(row.get("Valor", "0").replace(",", ".")),
                previous_value=float(str(row.get("ValorAnterior", "0").replace(",", ".")),
                gain=float(str(row.get("Ganho", "0").replace(",", ".")),
                gain_percent=float(str(row.get("Ganho (%)", "0").replace(",", ".")),
                title=title
            )
            session.add(quote)

    session.commit()