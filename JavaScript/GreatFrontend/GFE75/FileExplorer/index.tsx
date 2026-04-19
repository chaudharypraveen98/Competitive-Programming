import { useEffect, useState } from "react";
import { fileExplorerData } from "./data";
import "./index.css";

type FileItem = {
    name: string;
    children?: FileItem[];
    id: string;
    expanded?: boolean;
};

const FileItem = ({
    item,
    handleChange,
}: {
    item: FileItem;
    handleChange: (id: string) => void;
}) => {
    return (
        <div className="fileItem">
            <div className="fileItem__title">
                <div className="fileItem__label">{item?.name}</div>
                {item?.children ? (
                    <div
                        className="fileItem__status"
                        onClick={() => handleChange(item.id)}
                        role="button"
                        tabIndex={0}
                    >
                        [{item?.expanded ? "-" : "+"}]
                    </div>
                ) : null}
            </div>
            {item?.children && item?.expanded
                ? item?.children?.map((file) => {
                      return (
                          <div className="fileItem__children" key={file.id}>
                              <FileItem
                                  item={file}
                                  handleChange={handleChange}
                              />
                          </div>
                      );
                  })
                : null}
        </div>
    );
};

export default function FileExplorer({ data = fileExplorerData }) {
    const recursiveSort = (files: FileItem[]) => {
        // const sorted = [...files].sort((a, b) => (a.name > b.name ? 1 : b.name > a.name ? -1 : 0));
        const sorted: FileItem[] = [...files].sort((a, b) =>
            a.name.localeCompare(b.name),
        );
        return sorted?.map((file): FileItem => {
            return {
                ...file,
                children: file.children
                    ? recursiveSort(file.children)
                    : undefined,
            };
        });
    };
    const [currentFileState, setCurrentFileState] = useState<FileItem[]>(
        recursiveSort(data),
    );

    const recursiveUpdate = (id: string, state: FileItem[]) => {
        return state?.map((file: FileItem): FileItem => {
            if (file.id === id) {
                return {
                    ...file,
                    expanded: !file.expanded,
                };
            } else {
                return {
                    ...file,
                    children: file.children
                        ? recursiveUpdate(id, file.children)
                        : undefined,
                };
            }
        });
    };

    const handleChange = (id: string) => {
        setCurrentFileState((prev) => recursiveUpdate(id, prev));
    };

    return (
        <div>
            {currentFileState?.map((file) => (
                <FileItem
                    item={file}
                    handleChange={handleChange}
                    key={file.id}
                />
            ))}
        </div>
    );
}
