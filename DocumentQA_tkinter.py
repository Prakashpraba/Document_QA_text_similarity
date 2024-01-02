import fitz
import nltk 
import tkinter
from nltk import word_tokenize
from nltk.util import ngrams
from sentence_transformers import SentenceTransformer, util
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import *
from PIL import Image

my_text = None
input_entry = None
open_file = None 

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text

def extract_chunks(text):
    tokens = word_tokenize(text)    
    chunk_size=250
    overlap_size=20
    chunks = []
    for i in range(0, len(tokens), chunk_size - overlap_size):
        chunk = tokens[i:i + chunk_size]
        chunks.append(" ".join(chunk))   
    return chunks

def open_PDF():    
    global open_file
    try:   
        browse_text.set("loading...")
        open_file = filedialog.askopenfilename(
            initialdir="C:/gui/",
            filetypes=(
                ("PDF files", "*.pdf"),
                ("All Files", "*.*")
            )
        )
        if open_file:
            browse_text.set("Browse Files")
            button2 = tkinter.Button(options_frame, 
                background= '#3D3A4B',
                foreground= 'WHITE',
                text = 'Parse Document',
                activebackground= '#FFFFFF',
                activeforeground= 'BLACK',
                highlightthickness=2,
                width= 13, 
                height= 2,
                border= 0,
                font=('arial', 12,'bold'),
                cursor='hand2',
                command= chat_bot)
            button2.config(highlightbackground='BLACK', highlightcolor='BLACK')
            button2.place(x =88, y= 400) 
            label2 = Label(window, text= 'Document is uploaded ✔️ \n You can Parse the Document now', font=('arial', 15,'bold'), fg='#5FAD41')
            label2.place(x=150, y=300)         
    except Exception as e:
        print(f"Error: {e}")
    return open_file      

def chat_bot():
    global my_text, input_entry, open_file
    my_text = scrolledtext.ScrolledText(window, wrap=WORD, width=83, height=25)
    my_text.place(x= 10,y=120)

    input_entry = Entry(window, width=95)
    input_entry.place(x= 20, y= 550)

    send_button = Button(window, text="Send",background= '#36558F',
                        foreground= 'WHITE',
                        activebackground= '#FFFFFF',
                        activeforeground= 'BLACK',
                        highlightthickness=2,
                        width= 7, 
                        height= 1,
                        border= 0,
                        font=('arial', 9,'bold'),
                        command=process_question)
    send_button.place(x =600, y= 547)

    display_message(f"🤖: Howdy!\n", is_response=True,color='green', font_size=11)
    display_message(f"🤖: Document parsing is done, Pls ask your Questions!\n", is_response=True,color='green', font_size=11)

def sentence_transormer(question, chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    sentences1 = []
    sentences1.append(question)
    sentences2 = chunks

    embeddings1 = model.encode(sentences1, convert_to_tensor=True)
    embeddings2 = model.encode(sentences2, convert_to_tensor=True)

    cosine_scores = util.cos_sim(embeddings1, embeddings2)

    top_indices = cosine_scores.argsort(descending=True, axis=1)[:, :5]
    top_sentences = []
    for i in range(len(sentences1)):
        current_top_sentences = []
        for j in range(5):
            index = top_indices[i][j].item()
            score = cosine_scores[i][index].item()
            current_top_sentences.append((sentences2[index], score))
        top_sentences.append(current_top_sentences)

    return top_sentences

def process_question():
    global my_text, input_entry, open_file
    question = input_entry.get()
        
    pdf_text = extract_text_from_pdf(open_file)
    chunks = extract_chunks(pdf_text)
    responses = sentence_transormer(question, chunks)

    display_message(f"{question} :🧒 \n", is_user=True, color ='blue', font_size=10)
    display_message(f"🤖: The top 5 choices for '{question}'\n", is_response=True, color='green', font_size=10)
    for i, response in enumerate(responses[0], 1):
        sentence, score = response
        display_message(f"● Choice {i} for the given question:\n", is_response=True, color='green', font_size=10)
        display_message(f" {sentence} \n(Score: {score:.4f})\n", is_response=True, color='green', font_size=10)

    input_entry.delete(0, END)    

def display_message(message, is_response=False, is_user=False,color='black', font_size=10):
    global my_text
    tag = "response" if is_response else "user"
    justify = RIGHT if is_user else LEFT
    my_text.config(state=NORMAL)
    my_text.insert(END, f"{message}\n", tag)
    my_text.tag_configure(tag, justify=justify)
    my_text.tag_configure(tag, foreground= color, font=('Helvetica', font_size, 'bold'))
    my_text.see(END)
    my_text.config(state=DISABLED)

window = tkinter.Tk()
window.geometry('1000x600')
window.config(bg= '#E3DFFF')
window.title('Document QnA')

heading = Label( window , text="Document QA \n Sentence Similarity",width= 100, pady=20, font=('arial',20,'bold'))
heading.configure(background='#32213A',foreground='#FFFFFF')
heading.pack()    

options_frame = tkinter.Frame(window, bg= '#FFFFFF')
options_frame.pack(side=RIGHT)
options_frame.pack_propagate(False)
options_frame.configure(width=290, height=500)

img = PhotoImage(file = r"C:\Users\rr422792\Downloads\Hand coding-amico.png")
photo = img.subsample(9,9)
Label_img = Label(options_frame, image=photo,bg='#FFFFFF')
Label_img.place(x =40, y= 50)

label1 = Label(options_frame, text="Select PDF from your device" ,height=2, font=('arial',12,'bold'))
label1.configure(foreground='#3B413C', background='#FFFFFF')
label1.place(y=280, x=50)

browse_text = StringVar()
button1 = tkinter.Button(options_frame, 
            background= '#3D3A4B',
            foreground= 'WHITE',
            textvariable=browse_text,
            activebackground= '#FFFFFF',
            activeforeground= 'BLACK',
            width= 12, 
            height= 2,
            border= 0,
            font=('arial', 11,'bold'),
            cursor='hand2',
            command = open_PDF)
browse_text.set("Browse Files")
button1.place(x =100, y= 340 )


# self.title_font = tkfont.Font(family='Helvetica', size =18, weight="bold", slant ='italic')
window.mainloop()