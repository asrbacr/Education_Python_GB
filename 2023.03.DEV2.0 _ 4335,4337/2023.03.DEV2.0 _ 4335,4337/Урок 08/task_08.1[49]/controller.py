import view
import model


def menu():
    phone_book_main = []
    while True:
        choice = view.show_menu()
        if choice == "":
            print("до новых встреч")
            break
        elif choice == "c":
            rec = model.create_rec(*view.new_rec(mode = "new"))
            phone_book_main.append(rec)
        elif choice == "r":
            surname = view.surname()
            recs = model.select(phone_book_main, surname)
            view.show_recs(recs)
        elif choice == "u":
            surname = view.surname()
            recs = model.select(phone_book_main, surname)
            if recs:
                idx = phone_book_main.index(recs[0])
                rec = model.create_rec(*view.new_rec(mode = "update"))
                rec = model.merge(rec, recs[0])
                phone_book_main[idx] = rec
        elif choice == "d":
            surname = view.surname()
            recs = model.select(phone_book_main, surname)
            if recs:
                idx = phone_book_main.index(recs[0])
                phone_book_main.pop(idx)
        elif choice == "i":
            filename = view.file_name()
            recs = model.import_file(filename)
            phone_book_main.extend(recs)
        elif choice == "e":
            filename = view.file_name()
            model.export_file(filename, phone_book_main)
        elif choice == "s":
            view.show_all_recs(phone_book_main)
        else:
            print("Недопустимый пункт меню")
