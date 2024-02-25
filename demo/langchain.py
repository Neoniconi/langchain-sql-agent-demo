from langchain.chains import create_sql_query_chain
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_openai import ChatOpenAI

from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

def getLLM(model="gpt-3.5-turbo"):
    return ChatOpenAI(model=model, temperature=0)

def convertQuestionsToSql(db, llm, question = "How many employees are there"):
    chain = create_sql_query_chain(llm, db)
    return chain.invoke({"question": question})


def executeSqlQuery(db, llm, question = "How many employees are there"):
    execute_query = QuerySQLDataBaseTool(db=db)
    write_query = create_sql_query_chain(llm, db)
    chain = write_query | execute_query
    chain.invoke({"question": question})

def answerTheQuestions(db, llm, question = "How many employees are there"):
    answer_prompt = PromptTemplate.from_template(
    """Given the following user question, corresponding SQL query, and SQL result, answer the user question.

    Question: {question}
    SQL Query: {query}
    SQL Result: {result}
    Answer: """
    )
    execute_query = QuerySQLDataBaseTool(db=db)
    write_query = create_sql_query_chain(llm, db)

    answer = answer_prompt | llm | StrOutputParser()
    chain = (
        RunnablePassthrough.assign(query=write_query).assign(
            result=itemgetter("query") | execute_query
        )
        | answer
    )

    chain.invoke({"question": question})
