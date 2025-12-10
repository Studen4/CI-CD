import csv
import os

STATUS_MAP = {
    "Git Correct": 0,
    "Git Error": 1,
    "Git Exception": 2,
    "Git in test": 3
}


def validate_git_logs():
    csv_filename = 'git_logs.csv'

    if not os.path.exists(csv_filename):
        print(f"Помилка: Файл {csv_filename} не знайдено.")
        return

    passed_count = 0
    failed_count = 0

    try:
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)

            for i, row in enumerate(reader):
                line_num = i + 2

                if len(row) < 2:
                    continue

                status_str = row[0].strip()
                expected_code_str = row[1].strip()

                actual_code = STATUS_MAP.get(status_str)

                if actual_code is None:
                    failed_count += 1
                    continue

                try:
                    expected_code = int(expected_code_str)
                except ValueError:
                    failed_count += 1
                    continue

                is_correct = (actual_code == expected_code)

                result_status = "PASS" if is_correct else "FAIL"

                print(
                    f"{result_status} | Рядок {line_num}: "
                    f"Статус: {status_str} (Факт: {actual_code}). "
                    f"Очікуваний: {expected_code}. "
                    f"Результат: {is_correct}"
                )

                if is_correct:
                    passed_count += 1
                else:
                    failed_count += 1

    except Exception as e:
        print(f"Критична помилка: {e}")

    print("-" * 50)
    print(f"Результат перевірки: Успішно ({passed_count}), Помилок ({failed_count}).")


if __name__ == "__main__":
    validate_git_logs()