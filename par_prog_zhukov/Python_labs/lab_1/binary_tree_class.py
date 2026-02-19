# left_leaf = 2-(root-1), right_leaf = root*2
import sys
sys.path.append('c:\\Users\\nikit\\gerzen\\par_prog_zhukov\\Python_labs')
import Lab_3.MyExceptions as myExcept
import Lab_3.SimpleLogger
import Lab_3.SimpleLogger as Logger
import logging


class BinaryTree:
    def __init__(self, value, logger=None):
        self.value = value
        self.left = None
        self.right = None


simplelog = False
base_logger = logging.getLogger(__name__)
base_logger.setLevel(logging.INFO)

# настройка обработчика и форматировщика для logger2
handler = logging.FileHandler(f"Lab_3/{__name__}.log", mode='w')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# добавление форматировщика к обработчику
handler.setFormatter(formatter)
# добавление обработчика к логгеру
base_logger.addHandler(handler)

base_logger.info(f"Testing the custom logger for module {__name__}...")


def generate_binary_tree(height: int, root: int, logger=base_logger):
    if isinstance(logger, Lab_3.SimpleLogger.SimpleLog):
        simplelog = True
        logger.set_module(__name__)
    if height > 23:
        if logger:
            logger.error(f"Height is too big. Height is {height}")
        raise MyExcept.TooBigHeight("Height is too big")
    if height < 0:
        if logger:
            logger.error("height values invalid")
        raise myExcept.HeightLessZero(message="height values invalid")
    if not isinstance(root, int):
        if logger:
            logger.error("root values invalid")
        raise myExcept.BinaryTreeException(message="root values invalid")
    if not isinstance(height, int):
        if logger:
            logger.error("height values invalid")
        raise myExcept.BinaryTreeException(message="height values invalid")
    root = BinaryTree(root)
    tree_list = []
    tree = (root.value, tree_list)
    stack = [(root, 1, tree_list)]  # Стек для отслеживания текущего уровня и соответствующего узла

    while stack:
        node, level, node_tree = stack.pop()
        if level < height:
            left_value = 2 - (node.value - 1)
            right_value = node.value * 2

            node.left = BinaryTree(left_value)
            node.right = BinaryTree(right_value)
            l_child, r_child = ([], [])
            node_tree.append((left_value, l_child))
            node_tree.append((right_value, r_child))

            stack.append((node.left, level + 1, l_child))
            stack.append((node.right, level + 1, r_child))
    if logger:
        logger.info("bin tree was created")
    return tree


def print_binary_tree(tree, level=0, prefix='Root: '):
    if tree:
        print(' ' * level * 4 + prefix + str(tree[0]))
        for child in tree[1]:
            print_binary_tree(child, level + 1, prefix='Child: ')


def gen_rec_bin_tree(height: int, root: int, logger: Logger.SimpleLog = None):
    tree = {str(root): []}

    if height < 1:
        return tree
    else:
        l_r = 2 - (root - 1)
        r_r = root * 2
        a = gen_rec_bin_tree(root=l_r, height=height - 1)
        tree[str(root)].append(a)
        b = gen_rec_bin_tree(root=r_r, height=height - 1)
        tree[str(root)].append(b)
    if logger:
        logger.info("bin tree was created")
        logger.logout()
    return tree

{1:{2:{5:{}, 6:{}}, 3:{7:{}, 8:{}}}}
tree1 = BinaryTree(7)
tree2 = BinaryTree(8)
tree3 = BinaryTree(3)
tree3.right = tree1
tree3.left = tree2
tree21 = BinaryTree(5)
tree22 = BinaryTree(6)
tree4 = BinaryTree(2)
tree4.right = tree21
tree4.left = tree22
tree_m = BinaryTree(1)
tree_m.right = tree4
tree_m.left = tree3


tree1 = generate_binary_tree(3,2)
print_binary_tree(tree1)