import getpass
import os
import demo.db as db
import demo.langchain as lc

if __name__ == '__main__':
    print('hello')
    os.environ["OPENAI_API_KEY"] = getpass.getpass()
    
    db = db.getDB()
    llm = lc.getLLM()

    print(lc.convertQuestionsToSql(db=db, llm=llm))
    # print(lc.executeSqlQuery(db=db, llm=llm))
    # print(lc.answerTheQuestions(db=db, llm=llm))
