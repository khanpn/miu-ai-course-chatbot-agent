from ..utils.singleton import Singleton
from .langchain_helper import get_qa_chain


@Singleton
class QAChain:
    def __init__(self):
        print('Creating chain....')
        self._chain = get_qa_chain()

    def chain(self, question):
        return self._chain(question)['result']
