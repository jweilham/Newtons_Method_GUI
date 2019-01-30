from newton import Newton_GUI

#defines the main function to be run
def main():
    gui = Newton_GUI()#creates a new Tk class named app
    gui.mainloop()#run the app as a mainloop so it keeps running after calculations have been done

if __name__ == "__main__":#if the name of the class is main, run the main function
  main()
