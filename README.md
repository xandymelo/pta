# Practical Exam
Please **fork** this repo and **develop your server** based on the protocol described in pta.pdf file (in portuguese). Before coding, I suggest you carefully read the document spec and understand the protocol. Experiment the protocol, using paper and pencil, drawing examples of protocol usage.

Please develop your server code in the directory [pta-server][ptas]. The user list that must be accepted by the protocol must be read from the [pta-server/users.txt][ptau] file. The files to be served by your server are in the [pta-server/files][ptaa] directory. Please don't change these files and directories.

Your server code will be evaluated through an automatic testing tool. This way, in order to test your code you can use the [pta-client.py][ptac] file. This file makes some tests but it is not an extensive test. So, keep in mind that the actual evaluation will test other aspects of your protocol implementation.

You could use **any programming language**. But you must provide instructions in order to successfully run your code. Describe all stuff about libraries, interpreters, versions and so on. After finishing development, you must share the link of your github repo in the evaluation environment ([ava.ufrpe.br](http://ava.ufrpe.br/)).

[ptas]: <https://github.com/glaucogoncalves/pta/tree/master/pta-server>
[ptau]: <https://github.com/glaucogoncalves/pta/tree/master/pta-server/users.txt>
[ptaa]: <https://github.com/glaucogoncalves/pta/tree/master/pta-server/files>
[ptac]: <https://github.com/glaucogoncalves/pta/tree/master/pta-client.py>

------------------------------------------------------------------------------------------------------

Para testar o meu servidor pta, basta modificar a variável path, nas linhas 91 e 77 para o caminho do diretório da sua pasta 'files', e pronto!
Basta rodar o arquivo pta-servidor.py, e depois o pta-client.py.
