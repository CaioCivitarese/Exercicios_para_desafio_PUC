# Às vezes, algumas palavras como " localização " ou " internacionalização " são tão longas que escrevê-las várias vezes em um mesmo texto se torna bastante cansativo.

# Vamos considerar uma palavra muito longa se ela tiver estritamente mais de 10 caracteres. Todas as palavras muito longas devem ser substituídas por uma abreviação específica.

# Essa abreviação é feita assim: escrevemos a primeira e a última letra de uma palavra e, entre elas, o número de letras que separam a primeira da última. Esse número está no sistema decimal e não contém zeros à esquerda.

# Assim, " localização " será escrito como " l10n " e " internacionalização " será escrito como " i18n ".

# Sugere-se automatizar o processo de substituição de palavras por abreviações. Dessa forma, todas as palavras muito longas devem ser substituídas por abreviações, e as palavras que não são muito longas não devem sofrer alterações.

# Entrada
# A primeira linha contém um número inteiro n ( 1 ≤  n  ≤ 100 ). Cada uma das n linhas seguintes contém uma palavra. Todas as palavras são compostas por letras minúsculas do alfabeto latino e possuem de 1 a 100 caracteres.

# Saída
# Imprima n linhas. A i -ésima linha deve conter o resultado da substituição da i -ésima palavra dos dados de entrada.


