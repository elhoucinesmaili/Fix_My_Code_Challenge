#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 * free_dlistint_reverse - Frees a doubly linked list in reverse order
 *
 * @head: A pointer to the first element of the list
 */
void free_dlistint_reverse(dlistint_t *head)
{
    dlistint_t *node;

    /* Traverse to the last node */
    while (head && head->next)
        head = head->next;

    /* Free nodes in reverse order */
    while (head)
    {
        node = head;
        head = head->prev;
        free(node);
    }
}
