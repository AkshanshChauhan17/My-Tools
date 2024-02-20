import time
import pyautogui

def type_text(text, delay=0):
    """
    Function to simulate typing the given text.
    """
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(delay)

def main():
    # Give some time to focus on the input area
    time.sleep(5)

    # Example: Type the text "Hello, World!"
    text_to_type = """At first the professor scowled with concern. But then he said, that's all right. Run to my house. Tell my wife to give you one of my shirts. "Mrs. Esputa quickly fetched one of her husband's white shirts. But when Philip put it on, she began to exclaim, "Oh, dear! Gracious!" The shirt was so large that Philip was almost lost in it. Hastily Mrs. Esputa found a box of pins. In a twinkling, her nimble fingers pinned enough tucks in the shirt to make it fit Philip. They both heaved a big sigh of relief when the job was finished. Then, free from anxiety, Philip hurried back to the school. The concert finally began, and soon it was time for Philip's also. Stood up, placed the violin under his chin, and raised his bow. With horror he felt a pin pulling loose in the back of his shirt. But he recalled how many pins had been inserted in the shirt and thought, "Losing one won't matter. "Philip started to play. At first his right arm moved back and forth slowly, then more swiftly. Before long the pins that were holding his collar pulled out, The loose, large shirt collar began to creep up the back of Philip's head. Then the unruly sleeves grew looser and longer. Suddenly the shirt fell away from his neck. The audience began to laugh. In embarrassed confusion, Philip forgot what he was playing and stopped completely. The disaster so upset him that he rushed off the stage and sulked in a dark corner. Fighting back tears, he mumbled gloomily, "I wish I were dead Refreshments were served after the concert, but Philip was too busy to have any. He mingled with the crowd as quickly as he could, hoping to avoid Mr. Esputa. After a wistful look at the ice cream, Phillip was about to slink out when a booming voice behind him scoffed, "Well, Philip, you made a nice mess of it. " Philip turned and found himself face to face with his glowering teacher. With no sympathy for poor Philip, Mr. Esputa continued unreasonably, "No refreshments for you! You shouldn't have spent the day playing ball. You should have been preparing for the important work of the evening. You ought to be ashamed! MP hung his head, sighed heavily, and trudged home. The incident at Such an impression on him that he always remembered it. He never gain tried to mix work and play."""
    # Call the function to simulate typing
    type_text(text_to_type)

if __name__ == "__main__":
    main()