import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py --model <model_name>")
        return

    if sys.argv[1] == '--model':
        if len(sys.argv) < 3:
            print("Please specify a model name after --model")
            return
        model_name = sys.argv[2]
        # Đây là nơi bạn xử lý model_name, bạn có thể gọi các hàm hoặc thực hiện các thao tác khác tùy thuộc vào model_name
        print("Model name:", model_name)
    else:
        print("Unknown option:", sys.argv[1])

if __name__ == "__main__":
    main()
