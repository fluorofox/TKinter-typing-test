from tkinter import *
import random
import csv
 

TEXT_OPTIONS = [
    "The Arctic fox has remarkable adaptations for surviving in extreme cold. Its thick fur changes color with the seasons, turning white in winter to blend in with the snow, and brown in summer to match the tundra. It also has a keen sense of hearing, allowing it to locate and hunt small animals beneath the snow. During the harsh winter months, the Arctic fox's diet consists mainly of lemmings and other small rodents. In the summer, it scavenges on leftover carcasses and hunts birds and fish. These foxes are also known for their playful behavior, often engaging in games with each other to strengthen social bonds and develop hunting skills.",

    "Monarch butterflies are known for their incredible migration journey, traveling up to 3,000 miles from North America to central Mexico. These delicate insects rely on environmental cues, such as the angle of the sun, to navigate. Amazingly, the journey spans multiple generations, with each butterfly flying a portion of the route before laying eggs to continue the cycle. Monarch caterpillars feed exclusively on milkweed, which contains toxic compounds that make the butterflies distasteful to predators. This defense mechanism, combined with their bright orange and black coloration, warns potential threats to stay away. The monarch's lifecycle includes four stages: egg, larva (caterpillar), pupa (chrysalis), and adult, each with distinct and fascinating characteristics.",

    "Elephants are highly social animals, living in close-knit herds led by a matriarch. They communicate using a variety of vocalizations, including infrasound, which is too low for humans to hear. These powerful creatures have excellent memories and can recognize distant watering holes and former companions even after many years apart. Elephants also exhibit empathy and mourning behaviors, often showing compassion for injured or deceased herd members. Their trunks, an extension of their upper lip and nose, are incredibly versatile, used for breathing, smelling, touching, grasping, and producing sound. An elephant's diet consists mainly of grasses, fruits, and bark, and they can consume up to 300 pounds of food in a single day.",

    "Octopuses are renowned for their intelligence and problem-solving abilities. They have three hearts, and their blood is blue due to the presence of copper-based hemocyanin, which is more efficient at transporting oxygen in cold, low-oxygen environments. Octopuses can also change color and texture to blend in with their surroundings, an ability known as camouflage. They use this skill not only to avoid predators but also to communicate with other octopuses and to hunt prey. Octopuses have been observed using tools, such as coconut shells, for shelter and protection. Their ability to regenerate lost limbs is another fascinating aspect of their biology, highlighting their resilience and adaptability in the marine environment.",

    "Honeybees play a crucial role in pollination, transferring pollen from one flower to another, which helps plants reproduce. A single honeybee colony can pollinate millions of flowers each day. Honeybees communicate through a complex 'waggle dance,' which conveys information about the direction and distance of food sources to other members of the hive. Inside the hive, bees have specialized roles, including workers, drones, and the queen. Workers collect nectar and pollen, care for the young, and maintain the hive. Drones' primary role is to mate with a queen from another colony. The queen is the sole egg-layer, responsible for the colony's growth and sustainability. Honeybees also produce honey, which they make by converting nectar and storing it in hexagonal wax cells, providing a crucial food source for the colony during winter months.",

    "The aurora borealis, also known as the northern lights, is a mesmerizing display of lights in the sky predominantly seen in high-latitude regions around the Arctic. This phenomenon occurs when charged particles from the sun collide with atoms in Earth's atmosphere, causing bursts of light. These lights appear in various colors, primarily green and pink, but also red, yellow, blue, and violet. The shape of the aurora can vary from scattered patches to streamers, arcs, and even rippling curtains. The best time to view the northern lights is during the winter months when the nights are longest and the skies are darkest.",

    "Volcanoes are powerful natural features that result from the movement of tectonic plates. When magma from beneath the Earth's crust escapes through cracks, it leads to a volcanic eruption. These eruptions can vary from gentle flows of lava to explosive blasts that eject ash and gases high into the atmosphere. Some of the most famous volcanoes include Mount Vesuvius, Mount St. Helens, and Krakatoa. Volcanic eruptions can create new landforms and islands, like the Hawaiian Islands, but they can also be destructive, causing loss of life and property. The rich volcanic soil, however, is highly fertile and supports lush vegetation once the lava cools and weathers.",

    "Tsunamis are large ocean waves typically caused by underwater earthquakes, volcanic eruptions, or landslides. When the seafloor suddenly deforms and displaces the overlying water, it generates a series of waves that travel across the ocean at high speeds. Upon reaching shallow coastal waters, these waves can increase dramatically in height, resulting in massive destruction. The 2004 Indian Ocean tsunami is one of the deadliest in recorded history, highlighting the importance of early warning systems and disaster preparedness. Despite their destructive potential, tsunamis also contribute to coastal geology by redistributing sediment and reshaping shorelines over time.",

    "Hurricanes, also known as typhoons or cyclones depending on their location, are powerful tropical storms characterized by strong winds, heavy rain, and thunderstorms. They form over warm ocean waters and are fueled by the heat and moisture from the sea. The center of a hurricane, known as the eye, is relatively calm compared to the surrounding eyewall, where the most intense weather occurs. Hurricanes can cause widespread damage through storm surges, flooding, and high winds. They play a crucial role in regulating global temperatures by transferring heat from the tropics to the polar regions, thus contributing to the Earth's climate system.",

    "Earthquakes occur when there is a sudden release of energy in the Earth's crust, resulting in seismic waves that cause the ground to shake. Most earthquakes happen along fault lines, where tectonic plates meet. The magnitude of an earthquake is measured on the Richter scale, with each whole number increase representing a tenfold increase in measured amplitude. Major earthquakes can cause significant damage to buildings, infrastructure, and can trigger landslides and tsunamis. Despite their potential for destruction, earthquakes are also responsible for creating mountain ranges and are a crucial part of the planet's geological activity, helping scientists understand the dynamics of the Earth's interior.",

    "The construction of the Great Wall of China began in the 7th century BC and continued for centuries, with the most famous sections built during the Ming Dynasty. This colossal structure was intended to protect Chinese states from invasions by nomadic tribes. Stretching over 13,000 miles, the wall is not a single continuous structure but a series of walls and fortifications. Its construction involved millions of workers, including soldiers, peasants, and prisoners. The Great Wall stands as a testament to ancient Chinese engineering and strategic military planning, symbolizing resilience and the protection of civilization.",

    "The signing of the Magna Carta in 1215 was a landmark moment in the history of democracy. Forced upon King John of England by his barons, the Magna Carta was a charter of liberties that sought to limit the king's power and protect the rights of the nobility. It established the principle that everyone, including the king, was subject to the law. Though initially annulled by the Pope, the Magna Carta was reissued several times and became a cornerstone for the development of constitutional law, influencing documents such as the United States Constitution and the Universal Declaration of Human Rights.",

    "The Renaissance, spanning the 14th to the 17th century, was a period of remarkable cultural, artistic, and intellectual revival in Europe. Originating in Italy, the Renaissance marked the transition from the Middle Ages to modernity. It was characterized by a renewed interest in the classical art, literature, and learning of ancient Greece and Rome. Key figures of this era included Leonardo da Vinci, Michelangelo, and Galileo Galilei, whose works in art, science, and philosophy profoundly impacted Western civilization. The Renaissance laid the groundwork for the Scientific Revolution and the Enlightenment, shaping the course of European history.",

    "The invention of the printing press by Johannes Gutenberg in the mid-15th century revolutionized the dissemination of knowledge. Gutenberg's press, which used movable type, made it possible to produce books quickly and in large quantities, drastically reducing the cost of printed materials. This innovation played a crucial role in the spread of the Renaissance, the Reformation, and the Scientific Revolution. By making information more accessible, the printing press contributed to higher literacy rates and the democratization of knowledge, paving the way for the modern information age.",

    "The American Revolution (1775) was a pivotal conflict in which the thirteen American colonies fought for independence from British rule. Tensions had been building due to issues such as taxation without representation and British interference in colonial affairs. Key events like the Boston Tea Party and the battles of Lexington and Concord ignited the revolutionary spirit. Led by figures such as George Washington, Thomas Jefferson, and Benjamin Franklin, the revolution resulted in the founding of the United States of America. The Declaration of Independence, adopted on July 4, 1776, articulated the colonies' desire for self-governance and fundamental human rights.",

    "The French Revolution, which began in 1789, was a period of radical social and political upheaval in France. The revolution was driven by widespread discontent with the monarchy, economic hardship, and demands for democratic reforms. Key events included the storming of the Bastille, the Reign of Terror, and the rise of Napoleon Bonaparte. The revolution abolished the feudal system, established a republic, and inspired revolutionary movements worldwide. It also led to significant changes in French society, including the adoption of the Declaration of the Rights of Man and of the Citizen, which proclaimed the equality of all men and the principles of liberty, property, and security.",

    "The Industrial Revolution, beginning in the late 18th century, transformed economies and societies from agrarian-based to industrialized and urbanized. Originating in Britain, this period saw the development of new technologies such as the steam engine, spinning jenny, and power loom. These innovations greatly increased production capabilities and efficiency, leading to the growth of factories and mass production. The Industrial Revolution brought about profound changes in labor, with a shift from rural farming to urban factory work. While it improved overall living standards and spurred economic growth, it also led to harsh working conditions, prompting the rise of labor movements and reforms.",

    "The abolition of slavery in the United States was achieved through a combination of moral, political, and military efforts. The abolitionist movement, led by figures like Frederick Douglass, Harriet Tubman, and William Lloyd Garrison, tirelessly campaigned against the inhumanity of slavery. The Civil War, fought between the Union and Confederate states, was a pivotal conflict in this struggle. President Abraham Lincoln's Emancipation Proclamation in 1863 declared the freedom of slaves in Confederate-held territory. The 13th Amendment, ratified in 1865, abolished slavery throughout the United States, marking a significant victory for human rights and setting the stage for the long and ongoing struggle for racial equality.",

    "The signing of the Treaty of Versailles in 1919 officially ended World War I, one of the deadliest conflicts in human history. The treaty was negotiated among the Allied powers with little input from Germany, which was held responsible for the war and subjected to harsh reparations and territorial losses. The treaty aimed to prevent future conflicts but instead contributed to economic hardship and political instability in Germany. These conditions, along with the perceived injustices of the treaty, fueled the rise of Adolf Hitler and the outbreak of World War II. The Treaty of Versailles is often cited as a lesson in the complexities of peace negotiations and the importance of addressing the root causes of conflict.",

    "The moon landing on July 20, 1969, marked a monumental achievement in space exploration and human ingenuity. Apollo 11, the space mission conducted by NASA, successfully landed astronauts Neil Armstrong and Edwin 'Buzz' Aldrin on the moon while Michael Collins orbited above in the command module. Armstrong's famous words, 'That's one small step for man, one giant leap for mankind,' captured the significance of this event. The moon landing demonstrated the possibilities of space travel, sparked technological advancements, and fostered a sense of global unity and curiosity about the universe. It remains a defining moment in the history of science and exploration."
]
    

#------------------------------------------  GUI  ---------------------------------------------#
class Controller(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Fluorofox Typing Speed Test")
        self.geometry("700x700")
        #set the default font for labels and buttons to be "helvetica size 30"
        self.option_add("*Label.Font", "helvetica 30")
        self.option_add("*Button.Font", "helvetica 30")
        self.configure(bg="#d3d3d3") 
        container = Frame(self, height=700, width=700, bg="#d3d3d3")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.typing_speed = 0
        self.test_running = False
        self.frames = {}
        for F in (MenuPage, TestPage, CompletionPage, HighScorePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(MenuPage)
            
    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        # raises the current frame to the top
        frame.refresh()
        frame.tkraise()
        frame.focus_set()
 
 
        
class MenuPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#d3d3d3")
        self.controller = controller
        title_label = Label(self, text='Welcome to the typing test', fg='black', bg="#d3d3d3")
        title_label.place(relx=0.5, rely=0.4, anchor=CENTER)
        # Display a button to start the game and look at high scores
        start_button = Button(self, text='Start', command= lambda:self.controller.show_frame(TestPage))
        start_button.place(relx=0.5, rely=0.6, anchor=CENTER)
        highscore_button = Button(self, text='High Scores', command= lambda:self.controller.show_frame(HighScorePage))
        highscore_button.place(relx=0.5, rely=0.7, anchor=CENTER)
        
    def refresh(self):
        pass    



class TestPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#d3d3d3")
        self.controller = controller
        
    def refresh(self):
        for widget in self.winfo_children():
            widget.destroy()    
        self.text = random.choice(TEXT_OPTIONS).lower()
        self.seconds_left = 60
        self.countdown = 3
        self.controller.test_running = False
        self.splitPoint = 0
        self.left_side_label = Label(self, text=self.text[0:self.splitPoint], fg='grey', bg='dark grey')
        self.left_side_label.place(relx=0.5, rely=0.5, anchor=E)
        self.right_side_label = Label(self, text=self.text[self.splitPoint:], bg='dark grey')
        self.right_side_label.place(relx=0.5, rely=0.5, anchor=W)
        self.countdown_label = Label(self, text = f'Starting in {self.countdown}...', fg='red', bg="#d3d3d3")
        self.countdown_label.place(relx=0.5, rely=0.4, anchor=N)
        self.current_letter_label = Label(self, text=self.text[self.splitPoint], fg='grey', bg="#d3d3d3")
        self.current_letter_label.place(relx=0.5, rely=0.6, anchor=N)
        self.time_left_label = Label(self, text=f'{self.seconds_left} Seconds', fg='grey', bg="#d3d3d3")
        self.time_left_label.place(relx=0.5, rely=0.6, anchor=S)
        self.after(63000, self.stop_test)
        self.after(1000, self.countdown_second)
 
    
    def stop_test(self):
        self.controller.test_running = False
        self.controller.typing_speed = len(self.left_side_label.cget('text').split(' '))
        self.unbind('<Key>', self.key_press_binding_id)
        self.controller.show_frame(CompletionPage)


    def key_press(self, event=None): #event=None is used so that this can be called in various situations such as if you wanted to call it directly in the code as well as for a key press
        try:
            if event.char.lower() == self.right_side_label.cget('text')[0].lower():
                # Deleting one from the right side.
                self.right_side_label.configure(text=self.right_side_label.cget('text')[1:])
                # Adding one to the left side.
                self.left_side_label.configure(text=self.left_side_label.cget('text') + event.char.lower())
                #set the next Letter 
                self.current_letter_label.configure(text=self.right_side_label.cget('text')[0])
            else:
                self.left_side_label.configure(bg='red')
                self.right_side_label.configure(bg='red')
                self.after(200, self.reset_labels)
        except TclError:
            pass   
        
        
    def remove_second(self):
        self.seconds_left -= 1
        self.time_left_label.configure(text=f'{self.seconds_left} Seconds')
        if self.controller.test_running:
            self.after(1000, self.remove_second)


    def countdown_second(self):
        self.countdown -= 1
        if self.countdown > 0:
            self.countdown_label.config(text=f'Starting in {self.countdown}...')
            self.after(1000, self.countdown_second)
        else:
            self.countdown_label.config(text='Go!', fg='green')
            self.controller.test_running = True
            self.key_press_binding_id = self.bind('<Key>', self.key_press)
            self.after(1000, self.remove_second)


    def reset_labels(self):
        self.left_side_label.configure(bg='dark grey')
        self.right_side_label.configure(bg='dark grey')
        
        
class HighScorePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#d3d3d3")
        self.controller = controller
        

    def refresh(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.current_height = 0.15
        self.title_label = Label(self, text='High Scores', fg='black', bg="#d3d3d3")
        self.title_label.place(relx=0.5, rely=0.15, anchor=CENTER)
        with open('highscores.csv', newline='') as highscores_file:
            scores = csv.DictReader(highscores_file)
            for row in scores:
                self.current_height += 0.1
                name_label = Label(self, text=row['name'], fg='grey', bg="#d3d3d3")
                name_label.place(relx=0.3, rely=f"{self.current_height}", anchor=N)
                score_label = Label(self, text=row['score'], fg='grey', bg="#d3d3d3")
                score_label.place(relx=0.7, rely=f"{self.current_height}", anchor=N)
        self.menu_button = Button(self, text='Return to Menu', command=lambda:self.controller.show_frame(MenuPage))
        self.menu_button.place(relx=0.5, rely=0.8, anchor=CENTER)  
   
    
class CompletionPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.result_label = Label(self, text=f'Score: {self.controller.typing_speed} WPM', fg='white')
        self.result_label.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.restart_button = Button(self, text=f'Retry', command=lambda:controller.show_frame(TestPage))
        self.restart_button.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.highscore_button = Button(self, text='High Scores', command= lambda:controller.show_frame(HighScorePage))
        self.highscore_button.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.enter_name_entry = Entry(self, fg='white')
        self.enter_name_button = Button(self, text='Add', font=('helvetica', 16), width=5, command= lambda:self.add_high_score())

    def add_name(self):
        with open('highscores.csv', 'r', newline='') as highscores_file:
            fieldnames = ['name', 'score']
            reader = csv.DictReader(highscores_file, fieldnames=fieldnames)
            next(reader)
            scores = list(reader)
            for row in scores:
                if self.controller.typing_speed > int(row['score']) or len(scores) < 5:
                    self.result_label.configure(text=f'High Score!\nScore: {self.controller.typing_speed} WPM', fg='white')
                    self.enter_name_entry.place(relx=0.7, rely=0.5, anchor=E)
                    self.enter_name_button.place(relx=0.3, rely=0.5, anchor=W)
                    self.enter_name_entry.update()
                    self.enter_name_button.update()
                    self.enter_name_entry.focus_set()
    
    def add_high_score(self):
        name = self.enter_name_entry.get()
        updated=False
        with open('highscores.csv', 'r', newline='') as highscores_file:
            fieldnames = ['name', 'score']
            reader = csv.DictReader(highscores_file, fieldnames=fieldnames)
            next(reader)  # Skip header row
            scores = list(reader)
            for row in scores:
                if len(scores) < 5 or self.controller.typing_speed > int(row['score']):
                    scores.append({'name': f'{name}', 'score': f'{self.controller.typing_speed}'})
                    updated=True
                    break                
            if updated:
                scores = sorted(scores, key=lambda x: int(x['score']), reverse=True)[:5]
                with open('highscores.csv', 'w', newline='') as highscores_file:
                    writer = csv.DictWriter(highscores_file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(scores)
                self.enter_name_entry.delete(0, 'end')
                self.enter_name_entry.place_forget()
                self.enter_name_button.place_forget()
    
                
    def refresh(self):
        self.result_label.configure(text=f'Words per Minute: {self.controller.typing_speed}')
        if not self.controller.test_running:
            self.add_name()




if __name__ == "__main__":
    app = Controller()
    app.mainloop()