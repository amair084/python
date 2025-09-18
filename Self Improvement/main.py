import customtkinter as ctk
import tkinter as tk
import random
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Rank tiers
RANKS = ["F-", "F", "F+", "E-", "E", "E+", "D-", "D", "D+",
         "C-", "C", "C+", "B-", "B", "B+",
         "A-", "A", "A+", "S-", "S", "S+"]

colors = ["#63625C","#9C9191","#F0F0F0","#8CFF9F","#83FF4F","#3CFF1A","#FFC65C","#FFAB4A","#F26900",
          "#A8FFFA", "#6BFFF6", "#00E8FF", "#47A0FF", "#033AFF", "#3503FF", "#D463FF", "#FF526F",
          "#FF0000", "#FF7DC4", "#00BFA7", "#B30000"]

def xp_required(rank_index):
    return 100 * (2 ** rank_index)

class SubStat:
    def __init__(self, name, parent_category, difficulty):
        self.name = name
        self.xp = 0
        self.parent = parent_category
        self.difficulty = difficulty

    def add_xp(self, amount):
        self.xp += amount
        self.parent.add_xp(amount)

class Category:
    def __init__(self, name):
        self.name = name
        self.xp = 0
        self.rank_index = 0
        self.substats = []

    def add_xp(self, amount):
        self.xp += amount
        required = xp_required(self.rank_index)
        while self.xp >= required and self.rank_index < len(RANKS) - 1:
            self.xp -= required
            self.rank_index += 1
            required = xp_required(self.rank_index)

    def add_substat(self, substat_name, difficulty):
        sub = SubStat(substat_name, self, difficulty)
        self.substats.append(sub)
        return sub

class StatusApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("📜 Status Menu")
        self.resizable(False, False)

        # Categories
        self.categories = {
            "Fitness": Category("Fitness"),
            #"Islam": Category("Islam"),
            "Knowledge": Category("Knowledge"),
            "Discipline": Category("Discipline")
        }
        numCategories = 0

        for x in self.categories:
            numCategories += 1

        height = (750 / 4) * numCategories

        self.geometry("600x" + str(height))

        # Example substats
        self.categories["Fitness"].add_substat("Workout", "hard")
        self.categories["Fitness"].add_substat("Protein Intake", "easy")
        #self.categories["Islam"].add_substat("Quran Reading")
        #self.categories["Islam"].add_substat("Quran Memorization")
        #self.categories["Islam"].add_substat("Tafsir")
        #self.categories["Islam"].add_substat("Hadith Reading")
        #self.categories["Islam"].add_substat("Hadith Memorization")
        #self.categories["Islam"].add_substat("Adhkar")
        self.categories["Knowledge"].add_substat("Studying", "easy")
        self.categories["Knowledge"].add_substat("Testing", "medium")
        self.categories["Knowledge"].add_substat("Application", "medium")
        self.categories["Discipline"].add_substat("Focus Time", "easy")
        self.categories["Discipline"].add_substat("Restraint", "hard")
        self.categories["Discipline"].add_substat("Sleep on Time", "extreme")

        self.frames = {}

        logo_image = ctk.CTkImage(
            light_image=Image.open("logo.png"),
            dark_image=Image.open("logo.png"),
            size=(350, 70)  # adjust size as needed
        )

        # Place logo at the top of the window
        logo_label = ctk.CTkLabel(self, image=logo_image, text="")
        logo_label.pack(pady=0)

        # Build UI
        for idx, (cat_name, category) in enumerate(self.categories.items()):
            frame = self.build_category_frame(category)
            frame.pack(pady=10, padx=20, fill="x")
            self.frames[cat_name] = frame

    def build_category_frame(self, category):
        frame = ctk.CTkFrame(self)

        title = ctk.CTkLabel(frame, text_color=f"{colors[category.rank_index]}", text=f"{category.name} | Rank: {RANKS[category.rank_index]}", font=("Consolas", 20, "bold"))
        title.pack(pady=3)

        progress = ctk.CTkProgressBar(frame, width=500)
        progress.set(0)
        progress.pack(pady=3)

        sub_frame = ctk.CTkFrame(frame)
        sub_frame.pack(pady=3)

        for sub in category.substats:
            row = ctk.CTkFrame(sub_frame)
            row.pack(fill="x", pady=3)

            label = ctk.CTkLabel(row, text=sub.name, width=200, anchor="w")
            label.pack(side="left", padx=5)
            if sub.difficulty == "easy":
                btn = ctk.CTkButton(row, text="+2 XP", width=80, command=lambda s=sub, c=category, t=title, p=progress: self.add_xp_to_sub(s, c, t, p, 2))
            elif sub.difficulty == "medium":
                btn = ctk.CTkButton(row, text="+5 XP", width=80, command=lambda s=sub, c=category, t=title, p=progress: self.add_xp_to_sub(s, c, t, p, 5))
            elif sub.difficulty == "hard":
                btn = ctk.CTkButton(row, text="+10 XP", width=80, command=lambda s=sub, c=category, t=title, p=progress: self.add_xp_to_sub(s, c, t, p, 10))
            else:
                btn = ctk.CTkButton(row, text="+30 XP", width=80, command=lambda s=sub, c=category, t=title, p=progress: self.add_xp_to_sub(s, c, t, p, 30))
            btn.pack(side="right", padx=5)

        frame.title = title
        frame.progress = progress
        frame.category = category
        return frame

    def celebrate_rank_up(self):
        # Create canvas over the whole window
        canvas = tk.Canvas(
            self,
            bg=self.cget("bg"),  # match parent bg
            highlightthickness=0,
            bd=0
        )
        canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Load confetti images
        confetti_images = [
            tk.PhotoImage(file="confetti1.png"),
            tk.PhotoImage(file="confetti2.png"),
            tk.PhotoImage(file="confetti3.png"),
            tk.PhotoImage(file="confetti4.png")
        ]

        confetti = []
        for _ in range(60):
            x = random.randint(0, self.winfo_width())
            y = random.randint(-50, -0)
            img = random.choice(confetti_images)
            confetti.append({
                "id": canvas.create_image(x, y, image=img, anchor="nw"),
                "dx": random.choice([-2, -1, 1, 2]),  # sideways drift
                "dy": random.randint(2, 8),  # fall speed
                "img": img  # keep reference so image is not garbage collected
            })

        def animate():
            if not canvas.winfo_exists():  # stop if canvas destroyed
                return
            for c in confetti:
                canvas.move(c["id"], c["dx"], c["dy"])
                x, y = canvas.coords(c["id"])
                if y > self.winfo_height() + 30:
                    canvas.delete(c["id"])
            self.after(50, animate)

        animate()
        self.after(4000, canvas.destroy)

    def add_xp_to_sub(self, sub, category, title, progress, xp):
        previous_rank = category.rank_index
        sub.add_xp(xp)
        required = xp_required(category.rank_index)

        title.configure(text_color=f"{colors[category.rank_index]}", text=f"{category.name} | Rank: {RANKS[category.rank_index]}")
        progress.set(category.xp / required if required > 0 else 1)

        if category.rank_index > previous_rank:
            self.celebrate_rank_up()


if __name__ == "__main__":
    app = StatusApp()
    app.mainloop()
