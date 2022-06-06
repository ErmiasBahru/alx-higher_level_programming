#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - test if is a palindrome
 * @head: firts node of list
 * Return: 1 if is palindrome, 0 for no
 */
int is_palindrome(listint_t **head)
{
	listint_t *buscar;
	int con1 = 0, con2 = 0;
	int arr[4096];


	if (!head)
		return (0);
	buscar = *head;
	if (!*head || (*head)->next == NULL)
		return (1);

	for (con1 = 0; buscar; buscar = buscar->next, con1++)
		arr[con1] = buscar->n;
	for (con1--; con1 > con2; con1--, con2++)
	{
		if (arr[con2] == arr[con1])
			;
		else
			return (0);
	}
	return (1);
}
