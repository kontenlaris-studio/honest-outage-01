import os

LINE = "Everything is down and we don't know why. It worked at 9 a.m. That's the entire report. We will update it the moment we know more than you do."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {os.path.join(out_dir, 'entry.txt')} ({len(LINE)} characters)")

if __name__ == "__main__":
    main()
