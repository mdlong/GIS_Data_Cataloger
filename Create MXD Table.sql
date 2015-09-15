USE [CMTAGISStats]
GO

/****** Object:  Table [GDB].[MXDs]    Script Date: 9/15/2015 6:36:09 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [GDB].[MXDs](
	[Name] [nvarchar](100) NULL,
	[Path] [nvarchar](500) NULL,
	[Size] [float] NULL,
	[Created] [datetime] NULL,
	[Modified] [datetime] NULL,
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[CRC] [nchar](100) NULL
) ON [PRIMARY]

GO


