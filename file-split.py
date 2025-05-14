import os

def split_mbox(input_file, max_size_mb=100):
    # Use current working directory as output directory
    output_dir = os.path.dirname(os.path.abspath(__file__))
    base_output_name = "info-mbox-split"
    
    max_size_bytes = max_size_mb * 1024 * 1024
    part_number = 1
    current_size = 0
    current_messages = []
    message = []

    def write_part(messages, part_no):
        output_file = os.path.join(output_dir, f"{base_output_name}-{part_no}.mbox")
        with open(output_file, "w", encoding="utf-8") as out:
            for msg in messages:
                out.write("".join(msg))
        print(f"✅ Written: {output_file}")

    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if line.startswith("From ") and message:
                message_size = sum(len(l.encode('utf-8')) for l in message)
                if current_size + message_size > max_size_bytes:
                    write_part(current_messages, part_number)
                    part_number += 1
                    current_messages = []
                    current_size = 0
                current_messages.append(message)
                current_size += message_size
                message = [line]  # Start new message
            else:
                message.append(line)

        if message:
            message_size = sum(len(l.encode('utf-8')) for l in message)
            if current_size + message_size > max_size_bytes:
                write_part(current_messages, part_number)
                part_number += 1
                current_messages = []
            current_messages.append(message)

        if current_messages:
            write_part(current_messages, part_number)

    print("✅ All parts written successfully.")

# 🔁 Run with local file named "mbox" in same folder
split_mbox("mbox", max_size_mb=100)
