import React from 'react';
import { useQuery, TypedDocumentNode, DocumentNode, QueryHookOptions } from '@apollo/client';

interface ApolloRetrieverProps<Data, Vars> {
  query: DocumentNode | TypedDocumentNode<Data, Vars>;
  options?: QueryHookOptions<Data, Vars>;
  render: (data: Data) => JSX.Element;
}

export const ApolloRetriever = <Data, Vars>(props: ApolloRetrieverProps<Data, Vars>) => {
    const { query, options, render } = props;
    const { data, error, loading } = useQuery<Data, Vars>(
      query,
      options,
    );

    if (loading) {
        return <>'Loading'</>;
    }

    if (data) {
        return (
            <>
                {render(data)}
            </>
        );
    }

    if (error) {
        console.log(error);
    }

    return <></>;
}
