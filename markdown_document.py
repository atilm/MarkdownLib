from . import list_utilities

class MarkdownDocument:
    def __init__(self) -> None:
        self.content = []

    def getContent(self) -> list:
        return self.content

    def append(self, object) -> None:
        self.content.append(object)

class MarkdownSection:
    def __init__(self, title : str, level : int, lineNumber : int) -> None:
        self.title = title
        self.level = level
        self.lineNumber = lineNumber

class MarkdownTableRow:
    def __init__(self, cells : list, lineNumber : int) -> None:
        self._cells = cells
        self.lineNumber = lineNumber

    def getColumnCount(self) -> int:
        return len(self._cells)

    def get(self, columnIdx : int) -> str:
        return self._cells[columnIdx]

class MarkdownTable:
    def __init__(self, headerRow : MarkdownTableRow) -> None:
        self._headerRow = headerRow
        self.rows = []

    def getColumnCount(self) -> int:
        return self._headerRow.getColumnCount()

    def getColumnHeader(self, columnIndex : int) -> str:
        return self._headerRow.get(columnIndex)
    
    def getColumnWidths(self) -> list:
        columnWidths = self._getColumnWidths(self._headerRow._cells)
        
        for row in self.rows:
            rowWidths = self._getColumnWidths(row._cells)
            (columnWidths, rowWidths) = list_utilities.alignWidths(columnWidths, rowWidths)
            columnWidths = [max(p, c) for p, c in zip(columnWidths, rowWidths)]
        
        return columnWidths

    def getRowCount(self) -> int:
        return len(self.rows)
    
    def hasHeader(self, cells: list[str]) -> bool:
        if len(cells) != self.getColumnCount():
            return False
        
        for lhs, rhs in zip(cells, self._headerRow._cells):
            if lhs.strip() != rhs.strip():
                return False
        
        return True

    def getCell(self, rowIndex: int, columnIndex: int) -> str:
        return self.rows[rowIndex].get(columnIndex)
    
    def getRow(self, rowIndex: int) -> list[str]:
        if rowIndex < 0 or rowIndex >= len(self.rows):
            return []
        
        return self.rows[rowIndex]._cells

    def _getColumnWidths(self, rowEntries : list) -> list:
        return [len(s) for s in rowEntries]
