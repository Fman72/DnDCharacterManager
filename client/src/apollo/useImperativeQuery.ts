import { useQuery, DocumentNode, TypedDocumentNode } from '@apollo/client';

export const useImperativeQuery = (query: DocumentNode | TypedDocumentNode<any>) => {
  const { refetch } = useQuery(query, { skip: true });
	
  const imperativelyCallQuery = (variables?: any) => {
    return refetch(variables);
  } 
	
  return imperativelyCallQuery;
}