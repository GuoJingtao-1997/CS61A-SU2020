import tree as t

tree = t.tree
branches = t.branches
is_leaf = t.is_leaf
label = t.label
print_tree = t.print_tree


def generate_subsets():
    """
    Write a generator function generate_subsets that returns all subsets of the positive
    integers from 1 to n. Each call to this generator’s next method will return a list of
    subsets of the set [1, 2, ..., n], where n is the number of previous calls to next.

    >>> subsets = generate_subsets()
    >>> for _ in range(3):
    ...     print(next(subsets))
    ...
    [[]]
    [[], [1]]
    [[], [1], [2], [1, 2]]
    """
    lst, n = [[]], 1
    while True:
        yield lst
        lst.extend([l + [n]  for l in lst])
        n += 1

# def sum_paths_gen(t):
#     """
#     Implement sum paths gen, which takes in a tree t and and returns a generator which
#     yields the sum of all the nodes from a path from the root of a tree to a leaf.
#     You may yield the sums in any order.

#     >>> t1 = tree(5)
#     >>> next(sum_paths_gen(t1))
#     5
#     >>> t2 = tree(1, [tree(2, [tree(3), tree(4)]), tree(9)])
#     >>> sorted(sum_paths_gen(t2))
#     [6, 7, 10]
#     """
#     if is_leaf(t):
#         yield label(t)
#     for bs in branches(t):
#         for b in branches(bs):
#             yield label(bs) + label(t) + label(b)

# student and TA

class Student:
    students = 0  # This is a class attribute
    def __init__(self, name, ta):
        self.name = name  # This is a instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        ta.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

# Email send and receive

class Email:

    """We suggest that you approach this problem by first filling out the Email class, then
    fill out the register client method of Server, then implement the Client class,
    and lastly fill out the send method of the Server class.

    Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name
    
class Sever:

    """Each Server has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to
        """
        client = self.clients[email.recipient_name]
        client.receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        self.clients[client_name] = client

class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """
    def __init__(self, server, name):
        self.inbox = []
        self.name = name
        self.server = server
        self.server.register_client(self, self.name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox.append([email])

# Inheritance to avoid repeated code
class Pet:
    def __init__(self, name, owner):
        self.is_alive = True  # It's alive!!!
        self.name = name
        self.owner = owner
    
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Cat(Pet):
    """Below is a skeleton for the Cat class, which inherits from the Pet class. 
    To complete the implementation, override the init and talk methods and add a new
    lose_life method.
    Hint: You can call the init method of Pet to set a cat’s name and owner.
    """

    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner) # inherited construction of father
        self.lives = lives


    def talk(self):
        """ Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + " says meow!")

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        if self.is_alive:
            self.lives -= 1
            if not self.lives:
                self.is_alive = False
        else:
            print("The cat has no more lives to lose!")


class NoisyCat(Cat):
    """More cats! Fill in this implemention of a class called NoisyCat, which is just like a
    normal Cat. However, NoisyCat talks a lot – twice as much as a regular Cat!
    
    A Cat that repeats things twice."""   
    def talk(self):
        """Talks twice as much as a regular cat.

        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        super().talk()
        super().talk()

class A:
    def f(self):
        return 2
    
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1) # recursion in class

class B(A):
    def f(self):
        return 4
