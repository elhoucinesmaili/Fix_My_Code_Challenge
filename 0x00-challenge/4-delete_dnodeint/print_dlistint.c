#include <stdio.h>
#include "lists.h"

/**
 * print_dlistint_reverse - Prints a doubly linked list of integers in reverse
 *
 * @h: A pointer to the first element of a list
 *
 * Return: The number of elements printed
 */
size_t print_dlistint_reverse(const dlistint_t *h)
{
    size_t count = 0;

    /* Traverse to the last node */
    while (h && h->next)
        h = h->next;

    /* Traverse backward and print the list */
    while (h)
    {
        printf("%d\n", h->n);
        h = h->prev;
        count++;
    }

    return count;
}
