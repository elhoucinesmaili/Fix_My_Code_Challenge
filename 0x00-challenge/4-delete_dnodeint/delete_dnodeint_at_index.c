#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index_reverse - Deletes a node at a specific index in a doubly linked list
 *
 * @head: A pointer to the first element of a list
 * @index: The index of the node to delete
 *
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index_reverse(dlistint_t **head, unsigned int index)
{
    dlistint_t *node;
    unsigned int i;

    if (*head == NULL)
    {
        return (-1);
    }

    node = *head;

    /* Traverse to the desired node */
    for (i = 0; node && i < index; i++)
    {
        node = node->next;
    }

    /* Check if the index is valid */
    if (!node)
    {
        return (-1);
    }

    /* If the node to delete is the head */
    if (node == *head)
    {
        *head = node->next;
        if (*head)
        {
            (*head)->prev = NULL;
        }
    }
    else
    {
        /* Update the previous and next pointers to unlink the node */
        if (node->prev)
        {
            node->prev->next = node->next;
        }
        if (node->next)
        {
            node->next->prev = node->prev;
        }
    }

    /* Free the node */
    free(node);
    return (1);
}
