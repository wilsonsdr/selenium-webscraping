# Descrição do projeto

Este projeto eu desenvolvi para solucionar a dor do meu irmão, constantemente ele esquecia de bater o ponto em sua empresa, pensando nisso desenvolvi um script que realizasse essa tarefa para ele. Para aqueles que tem interesse, irei ensinar a criar o seu próprio script

<br>

# Ferramentas necessárias

- [Visual Studio Code](https://code.visualstudio.com/download) ou alguma outra IDE de sua preferência

- [Python](https://www.python.org/downloads/)

- [Selenium](https://www.geeksforgeeks.org/how-to-install-selenium-in-python/), que é um framework utilizado para testar aplicações web de forma automatizada

- [Geckodriver](https://github.com/mozilla/geckodriver/releases/), que é um mecanismo de navegador web utilizado para muitas aplicações

- [Navegador Firefox](https://www.mozilla.org/pt-BR/firefox/new/)

<br>

# Passo a passo

Baixado e instalado tudo corretamente, vamos ao que interessa 😃

Com o Visual Studio Code aberto, crie um arquivo python. Em seguida é necessário adicionar algumas bibliotecas necessárias

![Screenshot from 2022-09-14 19-17-28](https://user-images.githubusercontent.com/81364355/190272805-7b57e62d-23cd-460f-8261-e6701af0d7e7.png)

<br>

Próximo passo é adicionar o caminho do arquivo baixado, GeckoDriver, o paramêtro service_log_path é utilizado para não gerar log ao executar o script

![Screenshot from 2022-09-14 19-21-50](https://user-images.githubusercontent.com/81364355/190273429-abe953f4-0085-4edd-aa4f-b52979b57b36.png)

<br>

Como exemplo, criaremos um script para acessar a página do LinkedIn, preencher os seus dados e efetuar login, embora simples, você terá um breve entendimento de como usar a ferramenta e dai adiante, tudo dependerá da sua criatividade 😎

Com o link do site em mãos, utilizamos o método get para acessarmos a página

![Screenshot from 2022-09-14 20-04-27](https://user-images.githubusercontent.com/81364355/190278098-25ffabb1-b8fa-4306-83bb-a053b5680aec.png)

<br>

Agora precisamos identificar o elemento da página que corresponde ao email, senha e login. Basta clicar com o botão direito e clicar em inspecionar e encontrar o elemento que desejamos, há algumas formas de se obter a informação que precisamos, pelo ID, Class, CSS Seletor, XPATH, nesse caso, utilizaremos o XPATH

![Screenshot from 2022-09-14 20-35-28](https://user-images.githubusercontent.com/81364355/190280718-13a1eb01-2b8c-43a6-ab68-198334010cd7.png)

<br>

Com o método find_element colamos o XPATH dos elementos que pegamos, send_keys guardamos as nossas informações de email e senha, time.sleep será o tempo de delay em segundos

![Screenshot from 2022-09-14 20-40-30](https://user-images.githubusercontent.com/81364355/190281338-f03fd766-8897-4e55-8ff3-14b9655534e1.png)

<br>

E por último o XPATH do elemento de login mais o método click

![Screenshot from 2022-09-14 20-59-47](https://user-images.githubusercontent.com/81364355/190283129-5cf99889-4e7f-4a88-8a00-e25a3c89ed25.png)

<br>

Se você fez tudo certinho até aqui, seu script está pronto para rodar 🤩
