## Orientações

* escrever testes com unittest exige a importação do módulo e a criação de pelo menos uma classe que herda da classe "unittest.TestCase"
* o arquivo deve sermpre inciar com a palavra *test*
* a execução do teste pode se dar dentro do código ou com o executável do python (python -m unittest)
* convenção de nomenclatura:
  * as classes de teste usam camel-casing
  * os métodos de teste são em letras minúsculas
  * as palavras são separadas por um sublinhado

        class TestAccounts(unittest.TestCase):
            def test_creation(self):
                self.assertTrue(account.create())
            def test_deletion(self):
                self.assertTrue(account.delete())

* utilizar métodos de asserção em vez da função assert()
  * self.assertTrue(value): verifique se value é true.
  * self.assertFalse(value): verifique se value é false.
  * self.assertNotEqual(a, b): confirme que a e b não são iguais.
  * self.assertEqual(a, b): confirme que a e b são iguais
* os testes fazem com que o código seja responsável pelo próprio comportamento

## Tipos de testes

1. Teste de unidade:
    * Foco: testar a menor parte da lógica de código possível
    * Efeito colateral: velocidade
    * Aspectos:
        * Funções, métodos ou classes são testados o mais isolado possível, evitando a necessidade de configurar outras funções, métodos ou classes como um requisito
        * Nenhum serviço externo, como bancos de dados ou serviços de rede, é necessário para sua execução

2. Teste de integração:
    * Foco: testar a lógica que interagirá com outras partes da lógica em um projeto de código
    * Aspectos:
        * Não são tão rápidos quanto os testes de unidade e tendem a exigir mais configuração inicial antes de serem executados
        * Funções, métodos ou classes são testados com funcionalidade em outras funções, métodos ou classes
        * Um serviço externo pode ser usado, mas nem todos os serviços do aplicativo

3. Testes funcionais:
    * Foco: replicar o aplicativo o mais próximo possível do ambiente de produção
    * Aspectos:
        * Não são tão rápidos quanto os testes de unidade e tendem a exigir mais configuração inicial antes de serem executados
        * Funções, métodos ou classes são testados com funcionalidade em outras funções, métodos ou classes
        * Um serviço externo pode ser usado, mas nem todos os serviços do aplicativo.
        * Consomem tempo e muitos recursos

4. Integração contínua:
    * Não é um tipo de teste, mas é uma parte importante que tem a ver com cada tipo de teste
    * Um ambiente de CI executa testes automaticamente
    * A automação é o que define um ambiente consistente
    * Modos de execução:
        * Disparado por um evento
        * Executar em um agendamento
        * Gatilho manual

## Parametrização

* permite que você forneça facilmente entradas diferentes para um teste que executa a mesma declaração
* para usar a parametrização, você precisa importar pytest como uma biblioteca e usá-la como decorador na função

        import pytest   
        @pytest.mark.parametrize("item", ["No", "1", "10", "33", "Yes"])   #('arg_nomeado', [lista])
        def test_string_is_digit(item):
            assert item.isdigit()

**Vários argumentos:**

        @pytest.mark.parametrize("item, attribute", [("", "format"), (list(), "append")])
        def test_attributes(item, attribute):
            assert hasattr(item, attribute)

## Criando acessório para criação de arquivo temporário

* envolve o uso de um diretório temporário e o retorno do caminho para consumo de um teste

        import pytest
        import tempfile

        @pytest.fixture
        def tmp_file():
            def create():
                temp = tempfile.NamedTemporaryFile(delete=False)
            return temp.name
        return create   

* para chamar o acessório:

        import os
        def test_file(tmp_file):
            path = tmp_file()
            assert os.path.exists(path)

## Escopo

* *function:* é executado uma vez por teste
* *class:* é executado uma vez por classe
* *module:* é executado uma vez para um módulo
* *session:* é executado uma vez para uma sessão de teste

**Limpeza**: regisra uma função de limpeza para ser chamada após os testes:

        @pytest.fixture(scope="module")
        def tmp_file(request):
            temp = tempfile.NamedTemporaryFile(delete=False)
        def create():
            return temp.name
        def cleanup():
            os.remove(temp.name)
        request.addfinalizer(cleanup)
        return create

## Acessórios internos

* *cache:* permite criar e gerenciar um sistema de cache para testes
* *capsys:* auxiliar para captura e gravação de stderr e stdout
* *tmpdir:* criar e gerenciar diretórios temporários
* *monkeypatch:* aplicar patch em módulos, classes ou funções com comportamento específico