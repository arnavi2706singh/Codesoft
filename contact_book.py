import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
from datetime import datetime

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book - Professional Contact Manager")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # Contact storage
        self.contacts = []
        self.data_file = "contacts.json"
        
        # Load existing contacts
        self.load_contacts()
        
        # Setup GUI
        self.setup_gui()
        
        # Load contacts into the display
        self.refresh_contact_list()
    
    def setup_gui(self):
        # Main title
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        title_frame.pack(fill='x', padx=10, pady=(10, 0))
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="📞 Contact Book Manager", 
                              font=('Arial', 24, 'bold'), fg='white', bg='#2c3e50')
        title_label.pack(expand=True)
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Left panel for contact list
        left_panel = tk.Frame(main_frame, bg='white', relief='raised', bd=2)
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 5))
        
        # Search frame
        search_frame = tk.Frame(left_panel, bg='white')
        search_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(search_frame, text="🔍 Search Contacts:", font=('Arial', 12, 'bold'), 
                bg='white').pack(anchor='w')
        
        self.search_var = tk.StringVar()
        self.search_var.trace('w', self.on_search_change)
        search_entry = tk.Entry(search_frame, textvariable=self.search_var, 
                               font=('Arial', 11), width=40)
        search_entry.pack(fill='x', pady=(5, 0))
        
        # Contact list frame
        list_frame = tk.Frame(left_panel, bg='white')
        list_frame.pack(fill='both', expand=True, padx=10, pady=(0, 10))
        
        tk.Label(list_frame, text="📋 Contact List:", font=('Arial', 12, 'bold'), 
                bg='white').pack(anchor='w')
        
        # Treeview for contact list
        columns = ('Name', 'Phone', 'Email')
        self.contact_tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
        
        # Configure columns
        self.contact_tree.heading('Name', text='👤 Name')
        self.contact_tree.heading('Phone', text='📞 Phone')
        self.contact_tree.heading('Email', text='📧 Email')
        
        self.contact_tree.column('Name', width=200)
        self.contact_tree.column('Phone', width=150)
        self.contact_tree.column('Email', width=200)
        
        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.contact_tree.yview)
        self.contact_tree.configure(yscrollcommand=scrollbar.set)
        
        self.contact_tree.pack(side='left', fill='both', expand=True, pady=(5, 0))
        scrollbar.pack(side='right', fill='y', pady=(5, 0))
        
        # Bind selection event
        self.contact_tree.bind('<<TreeviewSelect>>', self.on_contact_select)
        
        # Right panel for contact details and operations
        right_panel = tk.Frame(main_frame, bg='white', relief='raised', bd=2, width=400)
        right_panel.pack(side='right', fill='y', padx=(5, 0))
        right_panel.pack_propagate(False)
        
        # Contact details frame
        details_frame = tk.LabelFrame(right_panel, text="📝 Contact Details", 
                                     font=('Arial', 12, 'bold'), bg='white')
        details_frame.pack(fill='x', padx=10, pady=10)
        
        # Form fields
        tk.Label(details_frame, text="Full Name:", font=('Arial', 10, 'bold'), 
                bg='white').grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.name_var = tk.StringVar()
        tk.Entry(details_frame, textvariable=self.name_var, font=('Arial', 10), 
                width=30).grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(details_frame, text="Phone Number:", font=('Arial', 10, 'bold'), 
                bg='white').grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.phone_var = tk.StringVar()
        tk.Entry(details_frame, textvariable=self.phone_var, font=('Arial', 10), 
                width=30).grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(details_frame, text="Email Address:", font=('Arial', 10, 'bold'), 
                bg='white').grid(row=2, column=0, sticky='w', padx=10, pady=5)
        self.email_var = tk.StringVar()
        tk.Entry(details_frame, textvariable=self.email_var, font=('Arial', 10), 
                width=30).grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(details_frame, text="Address:", font=('Arial', 10, 'bold'), 
                bg='white').grid(row=3, column=0, sticky='nw', padx=10, pady=5)
        self.address_text = tk.Text(details_frame, font=('Arial', 10), 
                                   width=30, height=3)
        self.address_text.grid(row=3, column=1, padx=10, pady=5)
        
        # Buttons frame
        buttons_frame = tk.Frame(right_panel, bg='white')
        buttons_frame.pack(fill='x', padx=10, pady=10)
        
        # Button styling
        button_style = {'font': ('Arial', 10, 'bold'), 'width': 15, 'height': 2}
        
        tk.Button(buttons_frame, text="➕ Add Contact", bg='#27ae60', fg='white',
                 command=self.add_contact, **button_style).pack(pady=5, fill='x')
        
        tk.Button(buttons_frame, text="✏️ Update Contact", bg='#3498db', fg='white',
                 command=self.update_contact, **button_style).pack(pady=5, fill='x')
        
        tk.Button(buttons_frame, text="🗑️ Delete Contact", bg='#e74c3c', fg='white',
                 command=self.delete_contact, **button_style).pack(pady=5, fill='x')
        
        tk.Button(buttons_frame, text="🔄 Clear Form", bg='#95a5a6', fg='white',
                 command=self.clear_form, **button_style).pack(pady=5, fill='x')
        
        # Statistics frame
        stats_frame = tk.LabelFrame(right_panel, text="📊 Statistics", 
                                   font=('Arial', 12, 'bold'), bg='white')
        stats_frame.pack(fill='x', padx=10, pady=10)
        
        self.stats_label = tk.Label(stats_frame, text="", font=('Arial', 10), 
                                   bg='white', justify='left')
        self.stats_label.pack(padx=10, pady=10)
        
        # Update statistics
        self.update_statistics()
        
        # Selected contact tracking
        self.selected_contact_id = None
    
    def load_contacts(self):
        """Load contacts from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    self.contacts = json.load(file)
            except:
                self.contacts = []
        else:
            # Add sample contacts
            self.contacts = [
                {
                    "id": 1,
                    "name": "John Doe",
                    "phone": "+1-555-0123",
                    "email": "john.doe@email.com",
                    "address": "123 Main St\nNew York, NY 10001",
                    "created": "2024-01-15"
                },
                {
                    "id": 2,
                    "name": "Jane Smith",
                    "phone": "+1-555-0456",
                    "email": "jane.smith@email.com",
                    "address": "456 Oak Ave\nLos Angeles, CA 90210",
                    "created": "2024-01-16"
                }
            ]
    
    def save_contacts(self):
        """Save contacts to JSON file"""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.contacts, file, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save contacts: {str(e)}")
    
    def refresh_contact_list(self, filtered_contacts=None):
        """Refresh the contact list display"""
        # Clear existing items
        for item in self.contact_tree.get_children():
            self.contact_tree.delete(item)
        
        # Use filtered contacts if provided, otherwise use all contacts
        contacts_to_show = filtered_contacts if filtered_contacts is not None else self.contacts
        
        # Add contacts to treeview
        for contact in contacts_to_show:
            self.contact_tree.insert('', 'end', values=(
                contact['name'],
                contact['phone'],
                contact['email']
            ), tags=(contact['id'],))
        
        # Update statistics
        self.update_statistics()
    
    def on_search_change(self, *args):
        """Handle search input changes"""
        search_term = self.search_var.get().lower()
        if not search_term:
            self.refresh_contact_list()
            return
        
        # Filter contacts based on search term
        filtered_contacts = []
        for contact in self.contacts:
            if (search_term in contact['name'].lower() or 
                search_term in contact['phone'].lower() or 
                search_term in contact['email'].lower()):
                filtered_contacts.append(contact)
        
        self.refresh_contact_list(filtered_contacts)
    
    def on_contact_select(self, event):
        """Handle contact selection from the list"""
        selection = self.contact_tree.selection()
        if selection:
            item = self.contact_tree.item(selection[0])
            contact_id = int(item['tags'][0])
            
            # Find and display the selected contact
            for contact in self.contacts:
                if contact['id'] == contact_id:
                    self.selected_contact_id = contact_id
                    self.display_contact(contact)
                    break
    
    def display_contact(self, contact):
        """Display contact details in the form"""
        self.name_var.set(contact['name'])
        self.phone_var.set(contact['phone'])
        self.email_var.set(contact['email'])
        
        self.address_text.delete('1.0', tk.END)
        self.address_text.insert('1.0', contact['address'])
    
    def clear_form(self):
        """Clear all form fields"""
        self.name_var.set('')
        self.phone_var.set('')
        self.email_var.set('')
        self.address_text.delete('1.0', tk.END)
        self.selected_contact_id = None
    
    def add_contact(self):
        """Add a new contact"""
        name = self.name_var.get().strip()
        phone = self.phone_var.get().strip()
        email = self.email_var.get().strip()
        address = self.address_text.get('1.0', tk.END).strip()
        
        # Validation
        if not name or not phone:
            messagebox.showerror("Error", "Name and phone number are required!")
            return
        
        # Check for duplicate phone numbers
        for contact in self.contacts:
            if contact['phone'] == phone:
                messagebox.showerror("Error", "A contact with this phone number already exists!")
                return
        
        # Create new contact
        new_contact = {
            "id": max([c['id'] for c in self.contacts], default=0) + 1,
            "name": name,
            "phone": phone,
            "email": email,
            "address": address,
            "created": datetime.now().strftime("%Y-%m-%d")
        }
        
        self.contacts.append(new_contact)
        self.save_contacts()
        self.refresh_contact_list()
        self.clear_form()
        
        messagebox.showinfo("Success", "Contact added successfully!")
    
    def update_contact(self):
        """Update the selected contact"""
        if not self.selected_contact_id:
            messagebox.showerror("Error", "Please select a contact to update!")
            return
        
        name = self.name_var.get().strip()
        phone = self.phone_var.get().strip()
        email = self.email_var.get().strip()
        address = self.address_text.get('1.0', tk.END).strip()
        
        # Validation
        if not name or not phone:
            messagebox.showerror("Error", "Name and phone number are required!")
            return
        
        # Check for duplicate phone numbers (excluding current contact)
        for contact in self.contacts:
            if contact['phone'] == phone and contact['id'] != self.selected_contact_id:
                messagebox.showerror("Error", "Another contact with this phone number already exists!")
                return
        
        # Update contact
        for i, contact in enumerate(self.contacts):
            if contact['id'] == self.selected_contact_id:
                self.contacts[i].update({
                    'name': name,
                    'phone': phone,
                    'email': email,
                    'address': address
                })
                break
        
        self.save_contacts()
        self.refresh_contact_list()
        self.clear_form()
        
        messagebox.showinfo("Success", "Contact updated successfully!")
    
    def delete_contact(self):
        """Delete the selected contact"""
        if not self.selected_contact_id:
            messagebox.showerror("Error", "Please select a contact to delete!")
            return
        
        # Confirmation dialog
        contact_name = None
        for contact in self.contacts:
            if contact['id'] == self.selected_contact_id:
                contact_name = contact['name']
                break
        
        if messagebox.askyesno("Confirm Delete", 
                              f"Are you sure you want to delete '{contact_name}'?"):
            # Remove contact
            self.contacts = [c for c in self.contacts if c['id'] != self.selected_contact_id]
            
            self.save_contacts()
            self.refresh_contact_list()
            self.clear_form()
            
            messagebox.showinfo("Success", "Contact deleted successfully!")
    
    def update_statistics(self):
        """Update the statistics display"""
        total_contacts = len(self.contacts)
        contacts_with_email = len([c for c in self.contacts if c['email']])
        
        stats_text = f"Total Contacts: {total_contacts}\n"
        stats_text += f"With Email: {contacts_with_email}\n"
        stats_text += f"Without Email: {total_contacts - contacts_with_email}"
        
        self.stats_label.config(text=stats_text)

def main():
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()

if __name__ == "__main__":
    main()