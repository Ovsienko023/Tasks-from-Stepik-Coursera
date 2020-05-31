function testFactorial(inputData) {

    if (inputData == 0) {return 1}
    if (inputData < 0)                             // Проверяем - положительное ли число
      throw "Число не должно быть меньше нуля";    // Если отрицательное - "бросаем" исключение
  
    return (inputData - 1)?(inputData * testFactorial(inputData - 1)):inputData;
  
  }

// console.log(testFactorial(-1))

// try {
//     // код, который нужно "попробовать"
//     // в этом коде может быть брошено исключение
//   } catch(exception_variable) {
//     // в этом месте пишется код, который выполняется только в случае обнаружения 
//     // исключения в предыдущем блоке "trу" 
//     // в случае возникновения исключения, в переменную exception_variable будет передан 
//     // код возникшей ошибки, например аргумент оператора throw
//   } finally {
//     // Код в этом блоке будет выполнен всегда, независимо от результата завершения блока try:
//     // и при завершении без ошибки, и при завершении с ошибкой, и при завершении по любому оператору перехода
//     // (break, continue, return)
//   }

try {
    throw new Error('Что-то пошло не так!');
} 
catch (e) {
    console.log(e.name + ': ' + e.message);
}
// Error: Что-то пошло не так!


function testErrorFunc(a, func) {
    try {
        var x = func(a);
    }
    catch(err) {
        return err.name;
    }
}

