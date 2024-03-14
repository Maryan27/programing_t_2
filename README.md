Рівень 2
Варіант 1
Зеник подарував Марічці ділянку городу розміром n на m, поділену на клітинки розміром 1 на 1 метр. У кожній клітинці Марічка посадила гарбузи, щоб дарувати їх залицальникам. Марічка почала садити гарбузи починаючи із верхньої лівої, і при досягненні правої межі - розверталась і рухалась справа наліво, як вказано в прикладі для m x n, де m - кількість рядків, а n - кількість стовпців:

1 2 3 4 8 7 6 5 9 10 11 12 16 15 14 13

Для садіння Марічка вирішила використати робота-садівника, який садить в кожну клітинку задану кількість зернят, які слід вказати як одномірний масив m x n. Якщо Марічка хоче посадити таку кількість гарбузів

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

Тоді роботу необхідно подати на всід таку послідовність (маршрут робота не незмінним):

1 2 3 4 8 7 6 5 9 10 11 12 16 15 14 13

Реалізуйте алгоритм, який отримає на вхід масив розміром m та n, в кожній клітинці якого знаходиться бажана кількість гарбузів та поверне одномірний масив, скільки зернин має висаджувати робот при руху згідно маршруту, вказаного в цій задчі (маршрут є незмінним)

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest . Ваш тести мають перевірити роботу алгоритму при значеннях m == n == 5, m =2, n =4, n = 1, m = 6
