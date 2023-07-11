#include "lists.h"

/**j
 * check_cycle - Check if a singly linked list contains a loop
 * @list: Pointer to head of a list
 * Return: 1 if there is a cycle, otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast && (fast = fast->next))
	{
		if (fast == slow)
			return (1);

		fast = fast->next;
		slow = slow->next;
	}
	return (0);
}
