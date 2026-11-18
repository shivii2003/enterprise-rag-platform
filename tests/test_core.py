from app.core import retrieve
def test_retrieve():
    assert retrieve('rag',[{'text':'hello'},{'text':'rag system'}])[0]['text']=='rag system'
