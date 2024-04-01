from fastapi  import FastAPI
from fastapi import HTTPException , status

app = FastAPI()


cursos ={
      1:{
          "nome" : "Python",
          "aulas": 20,
          "horas": 80,
          "instrutor": "Cleber"
      },

      2:{
           "nome" : "Java",
          "aulas": 15,
          "horas": 60,
          "instrutor": "Leonardo"
      },
      3:{
           "nome" : "Power bi",
          "aulas": 10,
          "horas": 30,
          "instrutor": "Camilla"
      }
 }

#outro get, fazer um get para cada coisa que desejo pegar
# @app.get('/cursos')
# async  def get_todos_cursos(cursos):
#      return cursos
 
@app.get('/cursos/{curso_id}') # endereço padrão
async def get_cursos(curso_id):
    try:
        curso_id = int(curso_id)
        curso= cursos[curso_id]
        curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Curso não encontrado.|')
    except  ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="So aceito inteiros....")
        



#isso faz com que execute automaticamente, e nao precise ficar matando o terminal e executando denovo
#__name__= variavel oculta
if __name__ =='__main__':#main significa principal
    import uvicorn
    uvicorn.run("main:app" ,host='0.0.0.0' , port=8000, reload=True)