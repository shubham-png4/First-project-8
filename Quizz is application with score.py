import random
import time

class Question:
    def __init__(self, question, options, correct_answer, category="General"):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.category = category
    
    def display(self):
        print(f"\n❓ {self.question}")
        for i, option in enumerate(self.options, 1):
            print(f"  {i}. {option}")

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.total_questions = 0
    
    def add_question(self, question, options, correct, category="General"):
        self.questions.append(Question(question, options, correct, category))
    
    def setup_quiz(self):
        # Math questions
        self.add_question("What is 15 × 4?", ["50", "60", "70", "80"], "60", "Math")
        self.add_question("What is 144 ÷ 12?", ["10", "11", "12", "13"], "12", "Math")
        self.add_question("What is the square of 9?", ["18", "27", "72", "81"], "81", "Math")
        
        # Science questions
        self.add_question("What is H2O?", ["Salt", "Water", "Sugar", "Oil"], "Water", "Science")
        self.add_question("Planet closest to Sun?", ["Earth", "Venus", "Mercury", "Mars"], "Mercury", "Science")
        
        # Geography questions
        self.add_question("Capital of India?", ["Delhi", "Mumbai", "Bangalore", "Chennai"], "Delhi", "Geography")
        self.add_question("Largest continent?", ["Africa", "Asia", "Europe", "America"], "Asia", "Geography")
        
        # General knowledge
        self.add_question("How many colors in rainbow?", ["5", "6", "7", "8"], "7", "General")
        self.add_question("Fastest land animal?", ["Lion", "Cheetah", "Horse", "Tiger"], "Cheetah", "General")
    
    def take_quiz(self):
        print("🎯 QUIZ TIME!")
        print("=" * 50)
        
        # Shuffle questions
        random.shuffle(self.questions)
        self.total_questions = len(self.questions)
        
        for i, q in enumerate(self.questions, 1):
            print(f"\nQuestion {i}/{self.total_questions} [{q.category}]")
            q.display()
            
            # Timer (15 seconds per question)
            print("⏱️  15 seconds...")
            time.sleep(1)  # In web editor, this might be limited
            
            try:
                answer = int(input("Your answer (1-4): "))
                
                if answer < 1 or answer > 4:
                    print("❌ Invalid option!")
                    continue
                
                selected_option = q.options[answer - 1]
                
                if selected_option == q.correct_answer:
                    print("✅ CORRECT!")
                    self.score += 10
                else:
                    print(f"❌ WRONG! Correct answer: {q.correct_answer}")
                
            except ValueError:
                print("❌ Enter a number!")
        
        self.show_results()
    
    def show_results(self):
        print("\n" + "=" * 50)
        print("📊 QUIZ RESULTS")
        print("=" * 50)
        print(f"Total Questions: {self.total_questions}")
        print(f"Correct Answers: {self.score / 10}")
        print(f"Score: {self.score}/{self.total_questions * 10}")
        print(f"Percentage: {self.score / (self.total_questions * 10) * 100:.1f}%")
        
        if self.score >= 80:
            print("🏆 Excellent! You're a genius!")
        elif self.score >= 60:
            print("🎉 Good job! Keep learning!")
        elif self.score >= 40:
            print("📚 Not bad, but practice more!")
        else:
            print("💪 Try again! You'll get better!")
        print("=" * 50)
    
    def menu(self):
        while True:
            print("\n" + "=" * 50)
            print("🎮 QUIZ APPLICATION")
            print("=" * 50)
            print("1. Take Quiz")
            print("2. View High Score")
            print("3. Exit")
            print("=" * 50)
            
            choice = input("Choose: ").strip()
            
            if choice == "1":
                self.take_quiz()
            elif choice == "2":
                print(f"\n🏆 Your Best Score: {self.score}/{self.total_questions * 10}")
            elif choice == "3":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice!")

# Run the quiz
quiz = Quiz()
quiz.setup_quiz()
quiz.menu()