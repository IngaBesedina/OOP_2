#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Вариант 1
Дополнительно к требуемым в заданиях операциям перегрузить
операцию индексирования [].
Максимально возможный размер списка задать константой.
В отдельном поле size должно храниться максимальное для данного объекта
количество элементов списка;реализовать метод size(),
возвращающий установленную длину. Если количество элементов списка
изменяется во время работы, определить в классе поле count.
Первоначальные значения size и count устанавливаются конструктором.
Создать класс BitString для работы с битовыми строками не более чем
из 100 бит. Битовая строка должна быть представлена списком типа int,
каждый элемент которого принимает значение 0 или 1.
Реальный размер списка задается как аргумент конструктора инициализации.
Должны быть реализованы операции:
and, or, xor, not. Реализовать сдвиг влево и сдвиг вправо на заданное
количество битов
"""


class BitString:
    MAX_SIZE = 100  # Максимально возможный размер битовой строки

    def __init__(self, bit_string: str = "0"):
        """Инициализация битовой строки."""
        if len(bit_string) > self.MAX_SIZE:
            raise ValueError(
                f"Битовая строка не может превышать {
                             self.MAX_SIZE} бит."
            )

        # Преобразуем строку в список бит
        self.bits = [int(bit) for bit in bit_string if bit in "01"]
        self.count = len(self.bits)

    def __getitem__(self, index: int) -> int:
        """Индексирование для получения бита по индексу."""
        if index < 0 or index >= self.count:
            raise IndexError("Индекс вне диапазона.")
        return self.bits[index]

    def __setitem__(self, index: int, value: int):
        """Индексирование для установки бита по индексу."""
        if index < 0 or index >= self.count:
            raise IndexError("Индекс вне диапазона.")
        if value not in (0, 1):
            raise ValueError("Значение должно быть 0 или 1.")

        self.bits[index] = value

    def size(self) -> int:
        """Возвращает текущий размер битовой строки."""
        return self.count

    def and_op(self, other):
        """Операция AND с другой битовой строкой."""
        min_size = min(self.count, other.count)
        result = [self.bits[i] & other.bits[i] for i in range(min_size)]
        return BitString("".join(map(str, result)))

    def or_op(self, other):
        """Операция OR с другой битовой строкой."""
        min_size = min(self.count, other.count)
        result = [self.bits[i] | other.bits[i] for i in range(min_size)]
        return BitString("".join(map(str, result)))

    def xor_op(self, other):
        """Операция XOR с другой битовой строкой."""
        min_size = min(self.count, other.count)
        result = [self.bits[i] ^ other.bits[i] for i in range(min_size)]
        return BitString("".join(map(str, result)))

    def not_op(self):
        """Операция NOT для текущей битовой строки."""
        result = [1 - bit for bit in self.bits]
        return BitString("".join(map(str, result)))

    def shift_left(self, n: int):
        """Сдвиг влево на n битов."""
        if n < 0:
            raise ValueError(
                "Количество битов для сдвига должно быть неотрицательным."
            )

        new_bits = self.bits[n:] + [0] * n
        return BitString("".join(map(str, new_bits)))

    def shift_right(self, n: int):
        """Сдвиг вправо на n битов."""
        if n < 0:
            raise ValueError(
                "Количество битов для сдвига должно быть неотрицательным."
            )

        new_bits = (
            [0] * n + self.bits[:-n] if n < self.count else [0] * self.count
        )
        return BitString("".join(map(str, new_bits)))

    def __repr__(self) -> str:
        """Строковое представление битовой строки."""
        return "".join(map(str, self.bits))


if __name__ == "__main__":
    bit_str1 = BitString("1101")
    bit_str2 = BitString("1011")

    print("Битовая строка 1:", bit_str1)
    print("Битовая строка 2:", bit_str2)

    # Операции
    print("AND:", bit_str1.and_op(bit_str2))
    print("OR:", bit_str1.or_op(bit_str2))
    print("XOR:", bit_str1.xor_op(bit_str2))
    print("NOT Битовой строки 1:", bit_str1.not_op())

    # Сдвиги
    print("Сдвиг влево на 2:", bit_str1.shift_left(2))
    print("Сдвиг вправо на 2:", bit_str1.shift_right(2))

    # Индексирование
    print("Бит по индексу 2 в Битовой строке 1:", bit_str1[2])
    bit_str1[2] = 0
    print("После изменения бита по индексу 2:", bit_str1)
