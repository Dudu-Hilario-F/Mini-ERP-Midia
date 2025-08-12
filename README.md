# Igreja Dashboard

Projeto Django 5.2 modular para gestão de igrejas.

## Estrutura Inicial
- Ambiente virtual: `.venv` já configurado
- Instalação de dependências: ativar ambiente com `.venv/scripts/activate` e usar `pip install <biblioteca>`
- Banco de dados: PostgreSQL (usar variável `DATABASE_URL` via django-environ)
- CSS: TailwindCSS
- Configurações separadas por ambiente: `settings/base.py`, `settings/dev.py`, `settings/staging.py`, `settings/prod.py`
- Apps separados por domínio
- Documentação de deploy: `DEPLOY.md`

## Próximos passos
1. Inicializar projeto Django com estrutura modular
2. Criar apps por domínio
3. Configurar TailwindCSS
4. Adicionar configurações de segurança
5. Preparar arquivos Docker
6. Documentar deploy