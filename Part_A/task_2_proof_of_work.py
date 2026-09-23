import hashlib
import time
import csv
import statistics

from pathlib import Path


DIFFICULTIES = [2, 3, 4, 5]
BLOCKS_PER_DIFFICULTY = 30


def calculate_hash(block_number, data, nonce):
    block_contents = f"{block_number}|{data}|{nonce}"
    return hashlib.sha256(block_contents.encode("utf-8")).hexdigest()


def mine_block(block_number, data, difficulty):
    target = "0" * difficulty
    nonce = 0
    attempts = 0
    start_time = time.perf_counter()

    while True:
        block_hash = calculate_hash(block_number, data, nonce)
        attempts += 1

        if block_hash.startswith(target):
            mining_time = time.perf_counter() - start_time
            return {
                "difficulty": difficulty,
                "block_number": block_number,
                "nonce": nonce,
                "hash": block_hash,
                "attempts": attempts,
                "mining_time": mining_time,
            }

        nonce += 1


def calculate_metrics(results):
    times = [result["mining_time"] for result in results]
    total_attempts = sum(result["attempts"] for result in results)
    total_time = sum(times)

    return {
        "difficulty": results[0]["difficulty"],
        "average_time": statistics.mean(times),
        "minimum_time": min(times),
        "maximum_time": max(times),
        "standard_deviation": statistics.stdev(times),
        "average_attempts": statistics.mean(
            result["attempts"] for result in results
        ),
        "hashes_per_second": total_attempts / total_time,
    }


def print_block_result(result):
    print(
        f"Block {result['block_number']:>2} | "
        f"Time: {result['mining_time']:.6f} s | "
        f"Attempts: {result['attempts']:>10,} | "
        f"Nonce: {result['nonce']:>10,}"
    )
    print(f"Valid hash: {result['hash']}")


def print_summary(metrics_by_difficulty):
    print("\nPERFORMANCE SUMMARY")
    print("=" * 119)
    print(
        f"{'Difficulty':<12}"
        f"{'Average (s)':>14}"
        f"{'Minimum (s)':>14}"
        f"{'Maximum (s)':>14}"
        f"{'Std dev (s)':>14}"
        f"{'Avg attempts':>18}"
        f"{'Hashes per second':>18}"
    )
    print("-" * 119)

    for metrics in metrics_by_difficulty:
        print(
            f"{metrics['difficulty']:<12}"
            f"{metrics['average_time']:>14.6f}"
            f"{metrics['minimum_time']:>14.6f}"
            f"{metrics['maximum_time']:>14.6f}"
            f"{metrics['standard_deviation']:>14.6f}"
            f"{metrics['average_attempts']:>18,.2f}"
            f"{metrics['hashes_per_second']:>18,.2f}"
        )


def save_results(all_results, metrics_by_difficulty):

    base_directory = Path(__file__).resolve().parent
    mining_directory = base_directory / "mining_files"
    mining_directory.mkdir(exist_ok=True)

    results_path = mining_directory / "mining_results.csv"
    summary_path = mining_directory / "mining_summary.csv"

    with results_path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        fieldnames = [
            "difficulty",
            "block_number",
            "nonce",
            "hash",
            "attempts",
            "mining_time",
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_results)

    with summary_path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=metrics_by_difficulty[0].keys(),
        )
        writer.writeheader()
        writer.writerows(metrics_by_difficulty)

    return results_path, summary_path


def main():
    all_results = []
    metrics_by_difficulty = []

    for difficulty in DIFFICULTIES:
        print(f"\nMINING 30 BLOCKS WITH DIFFICULTY {difficulty}")
        print(f"Target prefix: {'0' * difficulty}")
        print("-" * 100)

        difficulty_results = []

        for block_number in range(1, BLOCKS_PER_DIFFICULTY + 1):
            data = f"Transaction data for block {block_number}"
            result = mine_block(block_number, data, difficulty)
            difficulty_results.append(result)
            all_results.append(result)
            print_block_result(result)

        metrics_by_difficulty.append(calculate_metrics(difficulty_results))

    print_summary(metrics_by_difficulty)
    
    results_path, summary_path = save_results(
        all_results,
        metrics_by_difficulty,
    )

    print(f"\nDetailed results successfully saved to: {results_path}")
    print(f"Summary table successfully saved to: {summary_path}")


if __name__ == "__main__":
    main()
