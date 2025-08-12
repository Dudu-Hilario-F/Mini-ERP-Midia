# Guia de Deploy

Este projeto Django está pronto para deploy em Heroku, Railway, Vercel ou outros provedores compatíveis.

## Passos Gerais

1. Configure variáveis de ambiente (não versionar .env):
   - `DATABASE_URL` para PostgreSQL
   - `DJANGO_SECRET_KEY` para chave secreta
   - Outras variáveis conforme necessário

2. Instale dependências:
   - Ative o ambiente virtual: `.venv/scripts/activate`
   - Instale com `pip install -r requirements.txt`

3. Execute migrações:
   - `python manage.py migrate`

4. Colete arquivos estáticos:
   - `python manage.py collectstatic`

5. Execute o servidor:
   - `python manage.py runserver`

## Heroku
- Use Whitenoise para servir arquivos estáticos
- Configure `Procfile` e variáveis de ambiente

## Railway / Vercel
- Configure build e start scripts
- Adapte variáveis de ambiente conforme documentação do provedor

## Segurança
- Nunca versionar arquivos `.env` ou chaves secretas
- Use django-environ para ler variáveis

## Docker
- Utilize os arquivos `Dockerfile` e `docker-compose.yml` para desenvolvimento e CI