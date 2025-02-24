from manim import *


class CountingSortAnimation(Scene):
    def construct(self):
        # Show Python implementation first
        self.show_code_implementation()

        # Introduction sequence
        self.intro_sequence()
        self.wait(1)

        # Main sorting animation
        self.sorting_sequence()

    def show_code_implementation(self):
        # Title for code section
        code_title = Text(
            "Counting Sort: Code Implementation", color=BLUE).scale(0.8)
        code_title.to_edge(UP, buff=0.5)
        self.play(Write(code_title))

        # Python code for counting sort
        code_text = '''
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr
'''

        code = Code(
            code_string=code_text,
            tab_width=4,
            language="python",
            paragraph_config={"font": "Monospace", "font_size": 14},
        )
        code.next_to(code_title, DOWN)

        self.play(Create(code), run_time=2)

        # Transition text
        transition = Text("Now let's visualize how this algorithm works...",
                          color=GREEN).scale(0.7)
        transition.next_to(code, DOWN)
        self.play(Write(transition))

        # Clear screen for intro sequence
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )

    def intro_sequence(self):
        # Title
        title = Text("Understanding Counting Sort", color=BLUE).scale(1.2)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.scale(0.6).to_edge(UP))

        # Prerequisites text
        prereq_title = Text(
            "Before we begin, let's understand:", color=YELLOW).scale(0.8)
        prereq_title.next_to(title, DOWN, buff=0.8)

        prerequisites = VGroup(
            Text("1. We can only sort numbers (not letters or words)"),
            Text("2. Numbers must be positive integers (whole numbers)"),
            Text("3. We need to know the largest number in advance")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).scale(0.6)
        prerequisites.next_to(prereq_title, DOWN, buff=0.5)

        self.play(Write(prereq_title))
        self.play(Write(prerequisites), run_time=2)
        self.wait(1)

        # How it works
        how_title = Text("How Counting Sort Works:", color=GREEN).scale(0.8)
        how_title.next_to(prerequisites, DOWN, buff=0.8)

        steps = VGroup(
            Text("1. Count how many times each number appears"),
            Text("2. Create an array to store these counts"),
            Text("3. Use the counts to place numbers in correct positions")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).scale(0.6)
        steps.next_to(how_title, DOWN, buff=0.5)

        self.play(Write(how_title))
        self.play(Write(steps), run_time=2)
        self.wait(1)

        # Example introduction
        example = Text("Let's see this in action with an example!",
                       color=BLUE).scale(0.7)
        example.next_to(steps, DOWN, buff=0.8)

        self.play(Write(example))
        self.wait(1)

        # Clear screen for main animation
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )

    def sorting_sequence(self):
        # Initial array
        numbers = [4, 2, 2, 8, 3, 3, 1]
        max_val = max(numbers)

        # Create title with less vertical space
        title = Text("Counting Sort Visualization").scale(0.6)  # Smaller title
        title.to_edge(UP, buff=0.2)  # Very small top buffer
        self.play(Write(title), run_time=1)
        self.wait(0.5)

        # Add explanation text with reduced vertical spacing
        explanation = Text("Starting with unsorted numbers:").scale(
            0.5)  # Smaller text
        explanation.next_to(title, DOWN, buff=0.2)  # Very small buffer
        self.play(Write(explanation))

        # Create initial array visualization
        initial_squares = VGroup(*[
            Square(side_length=0.6).set_fill(
                BLUE, opacity=0.5)  # Smaller squares
            for _ in numbers
        ]).arrange(RIGHT, buff=0.15)  # Tighter spacing

        initial_nums = VGroup(*[
            Text(str(num), font_size=24).move_to(
                square)  # Explicit smaller font
            for num, square in zip(numbers, initial_squares)
        ])

        initial_array = VGroup(initial_squares, initial_nums)
        initial_array.next_to(explanation, DOWN, buff=0.3)  # Reduced buffer

        # Label for initial array
        init_label = Text("Initial Array:", font_size=24)  # Smaller text
        init_label.next_to(initial_array, LEFT)

        self.play(
            Create(initial_squares),
            run_time=1
        )
        self.wait(0.3)
        self.play(
            Write(initial_nums),
            Write(init_label),
            run_time=1
        )
        self.wait(1)

        # Create count array with explanation
        count_explanation = Text(
            # Smaller text
            "Creating count array (index = number, value = frequency):", font_size=24)
        count_explanation.next_to(
            initial_array, DOWN, buff=0.3)  # Reduced buffer
        self.play(Write(count_explanation))

        count_squares = VGroup(*[
            Square(side_length=0.6).set_fill(
                GREEN, opacity=0.3)  # Smaller squares
            for _ in range(max_val + 1)
        ]).arrange(RIGHT, buff=0.15)  # Tighter spacing

        count_nums = VGroup(*[
            Text("0", font_size=24).move_to(square)  # Smaller text
            for square in count_squares
        ])

        count_indices = VGroup(*[
            Text(str(i), color=RED, font_size=20).next_to(
                square, DOWN, buff=0.1)  # Smaller indices
            for i, square in enumerate(count_squares)
        ])

        count_array = VGroup(count_squares, count_nums, count_indices)
        count_array.next_to(count_explanation, DOWN,
                            buff=0.3)  # Reduced buffer

        # Label for count array
        count_label = Text("Count Array:", font_size=24)  # Smaller text
        count_label.next_to(count_array, LEFT)

        self.play(
            Create(count_squares),
            run_time=1
        )
        self.wait(0.3)
        self.play(
            Write(count_nums),
            Write(count_indices),
            Write(count_label),
            run_time=1
        )
        self.wait(0.5)

        # Update count array with explanation
        counting_explanation = Text(
            "Counting frequency of each number:", font_size=24)  # Smaller text
        counting_explanation.next_to(
            count_array, DOWN, buff=0.3)  # Reduced buffer
        self.play(Write(counting_explanation))

        counts = [0] * (max_val + 1)
        for num in numbers:
            counts[num] += 1
            new_num = Text(str(counts[num]), font_size=24)  # Smaller text
            new_num.move_to(count_nums[num])

            self.play(
                Flash(initial_nums[numbers.index(num)]),
                run_time=0.3
            )
            self.wait(0.2)

            self.play(
                Transform(count_nums[num], new_num),
                run_time=0.3
            )
            self.wait(0.3)

        self.wait(0.5)

        # Create output array with explanation
        output_explanation = Text(
            "Building sorted array using counts:", font_size=24)  # Smaller text
        output_explanation.next_to(
            counting_explanation, DOWN, buff=0.3)  # Reduced buffer
        self.play(Write(output_explanation))

        output = [0] * len(numbers)
        output_squares = VGroup(*[
            Square(side_length=0.6).set_fill(
                YELLOW, opacity=0.3)  # Smaller squares
            for _ in numbers
        ]).arrange(RIGHT, buff=0.15)  # Tighter spacing

        output_nums = VGroup(*[
            Text("", font_size=24).move_to(square)  # Smaller text
            for square in output_squares
        ])

        output_array = VGroup(output_squares, output_nums)
        output_array.next_to(output_explanation, DOWN,
                             buff=0.3)  # Reduced buffer

        # Label for output array
        output_label = Text("Sorted Array:", font_size=24)  # Smaller text
        output_label.next_to(output_array, LEFT)

        self.play(
            Create(output_squares),
            Write(output_label),
            run_time=1
        )
        self.wait(0.5)

        idx = len(numbers) - 1
        for i in range(max_val, -1, -1):
            for _ in range(counts[i]):
                new_num = Text(str(i), font_size=24)  # Smaller text
                new_num.move_to(output_squares[idx])

                self.play(
                    Flash(count_squares[i]),
                    run_time=0.3
                )
                self.wait(0.2)

                self.play(
                    Transform(output_nums[idx], new_num),
                    run_time=0.3
                )
                self.wait(0.2)
                idx -= 1

            if counts[i] > 0:
                self.wait(0.3)

        # Final explanation - properly positioned below output array
        final_text = Text(
            "And we're done! The array is now sorted!", color=GREEN, font_size=24)

        # Position final text below the output array with small buffer
        # and make sure it's centered horizontally
        final_text.next_to(output_array, DOWN, buff=0.3)
        final_text.set_x(0)  # Center horizontally in the frame

        # Ensure the text is visible by moving it up if it's too low
        # Typical bottom frame limit is around -4
        if final_text.get_bottom()[1] < -3.5:
            final_text.shift(UP * (abs(final_text.get_bottom()[1]) - 3.0))

        self.play(Write(final_text))
        self.wait(1.5)


if __name__ == "__main__":
    config.quality = "medium_quality"
    config.frame_rate = 30
    config.pixel_height = 720
    config.pixel_width = 1280
