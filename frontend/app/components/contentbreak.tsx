import React from 'react';

function ContentWithLineBreaks({content}:any) {
  const lines = content.split('\n');
  const paragraphs = lines.map((line:any, index:any) => <p className='py-1' key={index}>{line}</p>);

  return (
    <div>
      {paragraphs}
    </div>
  );
}

export default ContentWithLineBreaks;
