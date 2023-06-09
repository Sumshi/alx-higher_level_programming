#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly-linked list has a cycle.
 * @list: linked list to be checked.
 *
 * Return: 0 if no cycle or 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = NULL;
	listint_t *fast = NULL;

	/*Check if the list is null or contains only one node*/
	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;/*points to the first node*/
	fast = list->next;/*points to second node*/
	/*Traverse the list using slow and fast pointers*/
	while (fast != NULL && fast->next)
	{
		slow = slow->next;/*Move slow pointer by one step*/
		fast = fast->next->next;/*Move fast pointer by two steps*/

		/*If slow and fast pointers meet, there is a cycle in the list*/
		if (slow == fast)
			return (1);
	}

	/*If the loop completes without finding a cycle, return 0*/
	return (0);
}
