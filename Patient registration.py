from queue import Queue

patient_queue = Queue()

while True:
    print("\nMenu:")
    print("1. Register Patient")
    print("2. Remove Patient after Meeting Doctor")
    print("3. Display Patient Queue")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        patient_name = input("Enter patient name: ")
        patient_queue.put(patient_name)
        print("Patient", patient_name, "registered.")
    elif choice == '2':
        if patient_queue.empty():
            print("No patients in the queue.")
        else:
            removed_patient = patient_queue.get()
            print("Patient", removed_patient, "removed after meeting the doctor.")
    elif choice == '3':
        if patient_queue.empty():
            print("No patients in the queue.")
        else:
            print("Current Patient Queue:")
            queue_size = patient_queue.qsize()
            for _ in range(queue_size):
                patient = patient_queue.get()
                print(patient)
                patient_queue.put(patient)
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
