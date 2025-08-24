from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from workout_api.categorias.routers import router as categorias_router
from workout_api.atletas.routers import router as atletas_router
from workout_api.centro_treinamento.routers import router as centro_treinamento_router

app = FastAPI(
    title="Workout API - Desafio DIO",
    version="1.0.0",
    description="API para gerenciamento de atletas, categorias e centros de treinamento"
)

# ✅ Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # libera todas as origens (pode restringir depois se quiser)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Rotas principais
app.include_router(categorias_router, prefix="/categorias", tags=["Categorias"])
app.include_router(atletas_router, prefix="/atletas", tags=["Atletas"])
app.include_router(centro_treinamento_router, prefix="/centros", tags=["Centros de Treinamento"])

# ✅ Rota raiz só para teste
@app.get("/")
def read_root():
    return {"msg": "Workout API está rodando! 🚀"}
